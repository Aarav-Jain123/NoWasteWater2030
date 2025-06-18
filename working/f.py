# import asyncio


# async def fetch_data(delay):
#     print('hello')
#     await asyncio.sleep(delay)
#     print('bye')
#     return {'data': 'some data'}



# async def main():
#     print('start')
#     task = fetch_data(5)
#     print('recieved}')
#     result = await task
#     print(f'recieved {result}')

# asyncio.run(main())

import asyncio

async def fetch_data(id, sleep_time):
    print(f'Coroutine {id} started')
    await asyncio.sleep(sleep_time)
    return {'id': id, 'msg': f'Done collecting data from {id}'}

async def main():
    # task1 = asyncio.create_task(fetch_data(1, 2))
    # task2 = asyncio.create_task(fetch_data(2, 3))
    # task3 = asyncio.create_task(fetch_data(3, 1))
    
    
    
    # result1 = await task1
    # result2 = await task2
    # result3 = await task3
    
    # results = await asyncio.gather(fetch_data(1, 2), fetch_data(2, 3), fetch_data(3, 3))
    
    # for result in results:
        # print(result)
        
    tasks = []
    async with asyncio.TaskGroup() as tg:
        for i, sleep_time in enumerate([2., 1, 3], start=1):
            task = tg.create_task(fetch_data(i, sleep_time))
            tasks.append(task)
            
    results = [task.result() for task in tasks]
    
    for result in results:
        print(result)
    

asyncio.run(main())
