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
        url = 'https://example.com'
        fetchers = [asyncio.create_task(fetch_status(session, url)),
                    asyncio.create_task(fetch_status(
                        session, url)),
                    asyncio.create_task(fetch_status(session, url, delay=3))]

        done, pending = await asyncio.wait(fetchers, return_when=asyncio.FIRST_COMPLETED, timeout=2)

        print(f"Done task count: {len(done)}")
        print(f"Pending task count: {len(pending)}")

        for done_task in done:
            print(await done_task)

        for pending_task in pending:
            pending_task.cancel()


if __name__ == "__main__":
    asyncio.run(main())
