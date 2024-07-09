#!/usr/bin/python3

"""
  measure_time function with integers n and max_delay as arguments
  measures the total execution time for wait_n(n, max_delay)
"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ returns total_time / n """

    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - start) / 2
