import asyncio
import aiohttp
from aiohttp import ClientSession
from chapter_04 import fetch_status
from util import async_timed
from util import delay


@async_timed()
async def main() -> None:
    """
    """
    async with aiohttp.ClientSession() as session:
        urls = ['https://example.com', 'python://example.com']
        requests = [fetch_status(session, url) for url in urls]
        results = await asyncio.gather(*requests, return_exceptions=True)

        exceptions = [res for res in results if isinstance(res, Exception)]
        successful_results = [
            res for res in results if not isinstance(res, Exception)]

        print(f"All results :{results}\n")
        print(f"Finished successfully: {successful_results}\n")
        print(f"Threw exceptions: {exceptions}")

if __name__ == "__main__":
    asyncio.run(main())
