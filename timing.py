import functools
import time
from functools import wraps

# Todo - log the timing instead of printing it
def time_function(function):
    """
    Times the given function and prints how long it took for that function to run in microseconds

    Args:
        function: the function you want to time

    Returns:
        wrapper: It returns it's inner wrapper function which prints the time
    """
    @wraps(function)
    def wrapper(*args, **kwargs):
        """
        Times the given function and prints how long it took that function to run
        """
        start_time = time.perf_counter()
        result = function(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time_microseconds = (end_time - start_time) * 1_000_000  # Convert to microseconds
        print(f"{function.__name__} took {execution_time_microseconds:.2f} microseconds to run")
        return result
    return wrapper