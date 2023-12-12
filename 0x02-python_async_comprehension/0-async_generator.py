#!/usr/bin/env python3
"""
Write a couritine called async_generator that takes no arguments
The couritine will loop 10 times each time asychronously wait
1 second, then yield a random number btn 0 and 10.Use the
random module
"""
import asyncio
import random
import typing


async def async_generator() -> typing.Generator[float, None, None]:
    """
    generates random numbers btn 0 and 10
    """
    for i in range(10):
        await asyncio.sleep(1)  # Asynchronously wait for 1 sec
        yield random.uniform(0, 10)  # yield random no btn 0 and 10
