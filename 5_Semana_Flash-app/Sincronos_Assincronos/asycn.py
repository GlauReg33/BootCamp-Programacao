import time
import asyncio

async def asycn_task(task_id):
    print(f"Começando a tarefa {task_id}")
    await asyncio.sleep(2)
    print(f"Terminando a tarefa {task_id}")

async def main ():
    start_time = time.time()
    tasks = [asycn_task(1),asycn_task(2),asycn_task(3)]
    await asyncio.gather(*tasks)
    print(f"Tempo decorrido: {time.time() - start_time:.2f}s")

asyncio.run(main())