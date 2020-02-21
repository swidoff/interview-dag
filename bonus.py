import time
import random
import concurrent.futures
import threading
from task_graph import TaskGraph, make_graph


def execute_task(task):
    seconds = random.randint(1, 5)
    print(f"{threading.current_thread().name} {task}: Begin. Waiting {seconds} seconds.")
    time.sleep(seconds)
    print(f"{threading.current_thread().name} {task}: End")
    return task


def execute_dag(graph: TaskGraph, max_workers: int = 2):
    """
    Uses a concurrent.futures.ThreadPoolExecutor to call execute_task for each task in the dependency graph with as much
    concurrency as possible while still obeying the dependencies.
    """
    pass


if __name__ == '__main__':
    graph = make_graph()
    execute_dag(graph)
    assert graph.all_tasks_executed()
