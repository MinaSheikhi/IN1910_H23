import time
from functools import wraps


def printing(func):
    """Decorator for printing the output of a function."""
    name = func.__name__

    def printing_function(arg):
        output = func(arg)
        print(f"{name}({arg}) = {output}.")
        return output

    return printing_function


def timer(func):
    """Decorator for timing a function."""

    @wraps(func)
    def timed_function(arg):
        start_time = time.time()
        output = func(arg)
        elapsed = time.time() - start_time
        print(f"Elapsed time was {elapsed:.2g} seconds.")
        return output

    return timed_function


def memoize(func):
    """Decorator for memoizing a function."""
    storage = {}

    @wraps(func)
    def memoized(arg):
        if arg not in storage:
            storage[arg] = func(arg)
        return storage[arg]

    return memoized
