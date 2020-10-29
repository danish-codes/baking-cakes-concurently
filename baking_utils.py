import time
from functools import wraps

cakes = ["Chocolate", "Cheese", "Caramel"]

def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(end - start)
        return result
    return wrapper