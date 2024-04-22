#!/usr/bin/env python3
'''Basic async function'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''takes in an argument, waits for a random delay, then returns it.'''
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
