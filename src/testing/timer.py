from typing import Callable
from datetime import datetime as dt

def debugger(fun:Callable) -> Callable:
    def _wrapper():
        