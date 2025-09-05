import time
import asyncio


async def foo(n: int):
    print(f"Task {n} start")

    await asyncio.sleep(3)

    print(f"Task {n} stop")


async def tasker():
    task1 = asyncio.create_task(foo(n=1))
    task2 = asyncio.create_task(foo(n=2))

    await task1
    print("Что то сделал")
    await task2


async def awaiter():
    await foo(n=1)
    print("Что то сделал")
    await foo(n=2)


if __name__ == "__main__":
    start = time.perf_counter()
    asyncio.run(tasker())
    duration = time.perf_counter() - start
    print(f"Time: {duration}")
