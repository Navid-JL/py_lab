import asyncio
import aiohttp
from aiohttp import ClientSession
from chapter_04 import fetch_status
from util import async_timed
from util import delay


@async_timed()
async def main() -> None:
    async with aiohttp.ClientSession() as session:
        fetchers = [fetch_status(session, 'https://www.example.com'),
                    fetch_status(session, 'https://www.example.com'),
                    fetch_status(session, 'https://www.example.com')]

        done, pending = await asyncio.wait(fetchers)

        print(f"Done task count: {len(done)}")
        print(f"Pending task count: {len(pending)}")

        for done_task in done:
            result = await done_task
            print(result)

if __name__ == "__main__":
    asyncio.run(main())
