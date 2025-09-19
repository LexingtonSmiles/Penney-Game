import time
from typing import Callable
import os
from functools import wraps
import numpy as np




def measure_rw(fun: Callable) -> Callable:
    @wraps(fun)
    def wrapper(*args, **kwargs):
        start_write = time.perf_counter()
        result = fun(*args, **kwargs)
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
        end_read = time.perf_counter()
        read_duration = end_read - start_read

        # --- Compute Speeds ---
        write_speed = total_size / write_duration if write_duration else 0
        read_speed = total_size / read_duration if read_duration else 0

        # Return stats dictionary alongside the original result
        stats = {
            "function": fun.__name__,
            "num_files": len(file_paths),
            "total_size_bytes": total_size,
            "write_time": write_duration,
            "read_time": read_duration,
        }

        return  stats  # ← Return only stats here to simplify DataFrame construction
    return wrapper