import asyncio
import aiohttp
from aiohttp import ClientSession
from chapter_04 import fetch_status


async def fetch_status(session: ClientSession, url: str) -> int:
    # ten_millis = aiohttp.ClientTimeout(total=1.5)
    async with session.get(url) as result:
        return result.status


async def main():
    session_timeout = aiohttp.ClientTimeout(total=2, connect=1.5)

    async with aiohttp.ClientSession(timeout=session_timeout) as session:
        url = "https://www.example.com"
        status = await fetch_status(session, url)
        print(f'Status for {url} was {status}')

if __name__ == "__main__":
    asyncio.run(main())
