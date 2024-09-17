from asyncio import Future
# from util.delay_functions import delay


# async def main():


# if __name__ == "__main__":
#     asyncio.run(main())

my_future = Future()

print(f"Is my_future done? {my_future.done()}")

my_future.set_result(42)

print(f"Is my_future done? {my_future.done()}")
print(f"What is the result of my_future? {my_future.result()}")
