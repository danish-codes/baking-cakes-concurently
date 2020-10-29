from concurrent.futures.thread import ThreadPoolExecutor
from baking_utils import cakes, measure_time

import time


def make_a_cake(cake_type):
    print("Mixing the ingredients for a {} cake".format(cake_type))
    bake_a_cake()
    print("The {} Cake is ready".format(cake_type))

def bake_a_cake():
    time.sleep(10)

@measure_time
def run_in_multithreading(func, args, num_workers=1):
    results = ThreadPoolExecutor(num_workers).map(func, args)
    return list(results)

@measure_time
def run_in_sequence(func, args):
    return list(map(func, args))

if __name__ == "__main__":
    print("run in sequence: ")
    run_in_sequence(make_a_cake, cakes)
    print("run in multithreading: ")
    run_in_multithreading(make_a_cake, cakes, 3)

