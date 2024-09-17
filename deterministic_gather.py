import asyncio
import aiohttp
from aiohttp import ClientSession
from chapter_04 import fetch_status
from util import async_timed
from util import delay


@async_timed()
async def main() -> None:
    results = await asyncio.gather(delay(3), delay(1))
    print(results)


if __name__ == "__main__":
    asyncio.run(main())
