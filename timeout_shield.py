import asyncio
from util.delay_functions import delay


async def main():
    task = asyncio.create_task(delay(10))

    try:
        result = await asyncio.wait_for(asyncio.shield(task), timeout=5)
        print(result)
    except asyncio.exceptions.TimeoutError:
        print("Task took longer than five seconds, it will finish soon!")
        result = await task
        print(task)

if __name__ == "__main__":
    asyncio.run(main())
