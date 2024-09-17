import asyncio
import logging
import aiohttp
from aiohttp import ClientSession
from chapter_04 import fetch_status
from util import async_timed
from util import delay


@async_timed()
async def main() -> None:
    async with aiohttp.ClientSession() as session:
        api_a = fetch_status(session, 'https://example.com')
        api_b = fetch_status(session, 'https://example.com', delay=2)

        done, pending = await asyncio.wait([api_a, api_b], timeout=1)

        for task in pending:
            if task is api_b:
                print("API B too slow, cancelling")
                task.cancel()


if __name__ == "__main__":
    asyncio.run(main())
