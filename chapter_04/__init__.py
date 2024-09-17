import asyncio
from aiohttp import ClientSession
import aiohttp

from util import async_timed


# @async_timed()
async def fetch_status(session: ClientSession, url: str, delay: int = 0) -> int:
    # ten_millis = aiohttp.ClientTimeout(total=1.5)
    # async with session.get(url, timeout=ten_millis) as result:
    await asyncio.sleep(delay)
    async with session.get(url) as result:
        return result.status
