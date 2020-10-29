# baking-cakes-concurently

This repo demonstrates the difference concurency options in python
1. Multithreading 
2. Asyncio libary
3. Multiprocessing

`baking_cakes_in_multithreading.py` shows an example of baking 3 cakes in a sequence and in concurent way using multithreading.
We can see that running this script will yield better reaults for using multithreading.

`baking_cakes_async.py` shows an example of baking the same cakes using asyncio. We can see that the performance is about the same. The benefits of using asyncio in this case is that we can see clearly where do we pause and resume.

`baking_cakes_in_multiprocesses.py` presenting a cpu bound task and the difference in running it in a sequence using multithreading and using multiprocessing.
Running it in a sequence and with multiple threads will produce about the same results (the multithreading part might even take longer because of the overhead of using a thread pool) while using multiple process will give us much better reaults.
