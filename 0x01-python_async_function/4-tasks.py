#!/usr/bin/env python3
"""
Import wait_random from the prev python file  and write an async
routin called task_wait_n that takes 2 int args. You will spawn
wait_random n times with the specified max_delay
"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    creating tasks
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
