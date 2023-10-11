#!/usr/bin/env python3
"""
Async Generator
Write co-routine async_generator that takes two arguments
loops 10x, wait 1sec each time asynchronously
yield random number between 0-10 using random module
"""
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Co-routine async_generator
    yield random number 0-10
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
