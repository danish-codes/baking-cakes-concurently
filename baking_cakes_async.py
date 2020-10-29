from baking_cakes_in_multiprocesses import run_in_multithreading
from baking_cakes_in_multithreading import make_a_cake
from baking_utils import cakes, measure_time
import asyncio

async def bake_a_cake_async():
    await asyncio.sleep(10)

async def make_a_cake_async(cake_type):
    print("Mixing the ingredients for a {} cake".format(cake_type))
    await bake_a_cake_async()
    print("{} Cake is ready".format(cake_type))

async def bake_all_cakes():
    await asyncio.gather(*(make_a_cake_async(cake) for cake in cakes))

@measure_time
def run_async(func):
    asyncio.run(func())

if __name__ == "__main__":
    print("run in multithreading: ")
    run_in_multithreading(make_a_cake, cakes, 3)
    print("run async: ")
    run_async(bake_all_cakes)