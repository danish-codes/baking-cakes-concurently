from concurrent.futures.process import ProcessPoolExecutor
from baking_cakes_in_multithreading import run_in_sequence, run_in_multithreading
from baking_utils import cakes, measure_time

def make_a_cake_cpu_bound(cake_type):
    print("Mixing the ingredients for a {} cake".format(cake_type))
    bake_a_cake_cpu_bound()
    print("The {} Cake is ready".format(cake_type))

def bake_a_cake_cpu_bound():
    count = 0
    for i in range(200000000):
        count += i

@measure_time
def run_in_multiprocessing(func, args, num_workers=1):
    results = ProcessPoolExecutor(num_workers).map(func, args)
    return list(results)

if __name__ == "__main__":
    print("run in sequence: ")
    run_in_sequence(make_a_cake_cpu_bound, cakes)
    print("run in multithreading: ")
    run_in_multithreading(make_a_cake_cpu_bound, cakes, 3)
    print("run in multiprocessing: ")
    run_in_multiprocessing(make_a_cake_cpu_bound, cakes, 3)



