import asyncio
import time
from util.delay_functions import delay


async def hello_every_second() -> None:
    for i in range(2):
        await asyncio.sleep(1)
        print("I'm running other code while I'm waiting")


async def main() -> None:
    first_delay = asyncio.create_task(delay(3))
    second_delay = asyncio.create_task(delay(3))

    await hello_every_second()
    await first_delay
    await second_delay

start = time.time()
asyncio.run(main())
end = time.time()

print(f"The operation took {end - start:.4f}")
