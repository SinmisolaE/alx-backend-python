#!/usr/bin/env python3

"""
     an async routine called wait_n that takes in 2 int arguments
     (in this order): n and max_delay
     spawn wait_random n times with the specified max_delay
"""

import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """  return the list of all the delays (float values) """
    all_delay = await asyncio.gather(
            *tuple(map(lambda _: wait_random(max_delay), range(n)))
            )
    return all_delay
