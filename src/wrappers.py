import time
from typing import Callable
import os
from functools import wraps
import numpy as np

def timer(fun: Callable) -> Callable:
    @wraps(fun)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = fun(*args, **kwargs)
        end = time.perf_counter()
        print(f"{fun.__name__} took {end - start:.6f} seconds")
        return result
    return wrapper


def file_storage_tracker(fun: Callable) -> Callable:
    @wraps(fun)
    def wrapper(*args, **kwargs):
        result = fun(*args, **kwargs)
        
        # Ensure result is a list of file paths
        if isinstance(result, str):
            file_paths = [result]
        elif isinstance(result, (list, tuple)):
            file_paths = list(result)
        else:
            raise ValueError("Wrapped function must return a file path or list of file paths")
        
        # Compute total size
        total_size = 0
        for fp in file_paths:
            if os.path.exists(fp) and os.path.isfile(fp):
                total_size += os.path.getsize(fp)
            else:
                print(f"Warning: {fp} does not exist or is not a file")
        
        print(f"{fun.__name__} saved {total_size} bytes")
        return file_paths, total_size
    return wrapper


def measure_rw(fun: Callable)-> Callable: 
    @wraps(fun)
    def wrapper(*args, **kwargs):
        # --- WRITE phase ---
        start_write = time.perf_counter()
        result = fun(*args, **kwargs)  # Expected to return (file_paths, total_size)
        end_write = time.perf_counter()
        
        if not (isinstance(result, tuple) and len(result) == 2):
            raise ValueError("Function must return a tuple: (file_paths, total_size)")

        file_paths, total_size = result
        write_duration = end_write - start_write

        # --- READ phase ---
        start_read = time.perf_counter()
        for path in file_paths:
            if os.path.exists(path):
                _ = np.load(path, allow_pickle=True)
            else:
                print(f"⚠️ File not found: {path}")
        end_read = time.perf_counter()
        read_duration = end_read - start_read

        # --- Compute Speeds ---
        write_speed = total_size / write_duration if write_duration else 0
        read_speed = total_size / read_duration if read_duration else 0

        # --- Print Summary ---
        print(f"Read/Write Performance for `{fun.__name__}`:")
        print(f"Number of files:     {len(file_paths)}")
        print(f"Total size:          {total_size / 1_000_000:.3f} MB")
        print(f"Write time:          {write_duration:.6f} seconds")
        print(f"Write speed:         {write_speed / 1_000_000:.3f} MB/s")
        print(f"Read time:           {read_duration:.6f} seconds")
        print(f"Read speed:          {read_speed / 1_000_000:.3f} MB/s")

        return result  # Return original output so function still behaves normally
    return wrapper