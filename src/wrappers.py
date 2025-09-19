import time
from typing import Callable
import os
from functools import wraps

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
