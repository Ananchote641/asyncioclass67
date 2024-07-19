import asyncio
from random import random

async def cook_rice():
    time_taken = 1 + random()
    print(time_taken)
    await asyncio.sleep(time_taken)
  #  print(time_taken)
    return  f'cook_rice:  {time_taken}'

async def cook_noodle():
    time_taken = 1 + random()
    print(time_taken)
    await asyncio.sleep(time_taken)
   # print(time_taken)
    return  f'cook_noodle:  {time_taken}'

async def cook_curry():
    time_taken = 1 + random()
    print(time_taken)
    await asyncio.sleep(time_taken)
   # print(time_taken)
    return  f'cook_curry:  {time_taken}'

async def main():
    tasks = [
        asyncio.create_task(cook_rice()),
        asyncio.create_task(cook_noodle()),
        asyncio.create_task(cook_curry())
    ]
    
    

    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    print("Done")
    for task in done:
        
        time_taken = task.result()
        print(time_taken)

    print("Waitting")
    for task in pending:
        
       # dish, time_taken = task.result()\
        re = await task
        # print(f'-{dish} is completed in {time_taken:.10f}')
        # print(f'{dish} : Finished cooking')
        print(re)
    # print(f'Completed task: {len(done)} task.')    
    # # Print the time taken for each completed task
    # for task in done:
    #     dish, time_taken = task.result()
    #     print(f'{dish} : cooking {time_taken:.10f}')
        
    # print(f'Uncompleted task: {len(pending)} tasks.')

    # for task in pending:
    #     task.cancel()

asyncio.run(main())
