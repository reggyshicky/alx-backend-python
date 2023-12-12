#!/usr/bin/env python3
"""
Import async_generator for the previous tadk and then write
a couritine called async_comprehension that takes no arguments
The couritine will collect 10 random numbers using an async
comprehensing over async_generator, then return 10 random
numbers
"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Return lists of values yielded by asynch_generator"""
    return [item async for item in async_generator()]
