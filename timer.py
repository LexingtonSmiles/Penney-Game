import time
from typing import Callable

def timer(fun: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = fun(*args, **kwargs)
        end = time.perf_counter()
        print(f"{fun.__name__} took {end - start:.6f} seconds")
        return result
    return wrapper
