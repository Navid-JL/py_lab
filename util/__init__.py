import time
import functools
import asyncio
from collections.abc import Callable
from typing import Any


def async_timed():
    def wrapper(func: Callable) -> Callable:
        @functools.wraps(func)
        async def wrapped(*args, **kwargs) -> Any:
            print(f"starting {func} with args {args} {kwargs}")
            start = time.time()
            try:
                return await func(*args, **kwargs)
            finally:
                end = time.time()
                total = end - start
                print(f"finished {func} in {total:.4f} second(s)")
        return wrapped
    return wrapper


async def delay(delay_seconds: int) -> int:
    print(f"Sleeping for {delay_seconds} second(s)")
    await asyncio.sleep(delay_seconds)
    print(f"Finished sleeping for {delay_seconds} second(s)")
    return delay_seconds
