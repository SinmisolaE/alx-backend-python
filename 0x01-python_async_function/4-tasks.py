#!/usr/bin/env python3

"""
     an async routine called wait_n that takes in 2 int arguments
     (in this order): n and max_delay
     spawn task_wait_random n times with the specified max_delay
"""

import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """  return the list of all the delays (float values) """
    all_delay = await asyncio.gather(
            *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
            )
    return sorted(all_delay)
