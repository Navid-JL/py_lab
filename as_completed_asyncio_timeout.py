import asyncio
import aiohttp
from aiohttp import ClientSession
from chapter_04 import fetch_status
from util import async_timed
from util import delay


@async_timed()
async def main() -> None:
    async with aiohttp.ClientSession() as session:
        fetchers = [fetch_status(session, 'https://www.example.com', 1),
                    fetch_status(session, 'https://www.example.com', 10),
                    fetch_status(session, 'https://www.example.com', 10)]

        for done_task in asyncio.as_completed(fetchers, timeout=4):
            try:
                result = await done_task
                print(result)
            except asyncio.TimeoutError:
                print("We got a timeout error")

        print("-------------------------------------")
        for task in asyncio.tasks.all_tasks():
            print(task)

if __name__ == "__main__":
    asyncio.run(main())
