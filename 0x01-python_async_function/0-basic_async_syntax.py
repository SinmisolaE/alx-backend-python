#!/usr/bin/env python3

"""
  takes in an integer argument 'max delay'
  that waits for a random delay between 0 and max_delay
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ returns max_delay """
    time = random.uniform(0, max_delay)
    await asyncio.sleep(time)
    return time
