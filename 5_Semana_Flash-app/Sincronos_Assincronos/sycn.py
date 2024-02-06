import time

def sycn_task(task_id):
    print(f"Começando  a tarefa {task_id}")
    time.sleep(2)
    print(f"Terminando a tarefa {task_id}")

start_time = time.time()

sycn_task(1)
sycn_task(2)
sycn_task(3)

print(f"Tempo decorrido: {time.time() - start_time:.2f}s")