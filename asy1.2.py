import asyncio

async def fibonacci(n):
    await asyncio.sleep(1)
    a, b = 0, 1
    if n <= 1:
        return n
    else:
        for i in range(1, n):
            c = a + b
            a = b
            b = c
        return b

async def main():
    n = 10
    coros = [asyncio.create_task(fibonacci(i)) for i in range(n)]
    
    # ใช้ asyncio.wait แทน asyncio.gather
    done, pending = await asyncio.wait(coros, return_when=asyncio.ALL_COMPLETED)
    
    # ดึงผลลัพธ์จาก tasks ที่เสร็จแล้ว
    results = [task.result() for task in coros]
    
    print(results)

asyncio.run(main())
