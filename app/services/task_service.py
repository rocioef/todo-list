from app.models.task import Task, Status
from app.repositories.task_repository import load_tasks, save_tasks

def get_all_tasks():
    return load_tasks()

def get_next_id(tasks):
    if not tasks:
        return 1
    return max(task.id for task in tasks) + 1

def create_task(description):
    tasks = load_tasks()

    task = Task(
        id=get_next_id(tasks),
        description=description
    )

    tasks.append(task)
    save_tasks(tasks)

    return task

def find_task_by_id(tasks, task_id):
    for task in tasks:
        if task.id == task_id:
            return task
    return None

def start_task(task_id):
    tasks = load_tasks()
    task = find_task_by_id(tasks, task_id)

    if task is None:
        return None

    task.status = Status.IN_PROGRESS
    save_tasks(tasks)

    return task

def complete_task(task_id):
    tasks = load_tasks()
    task = find_task_by_id(tasks, task_id)

    if task is None:
        return None

    task.status = Status.COMPLETE
    save_tasks(tasks)

    return task

def delete_task(task_id):
    tasks = load_tasks()
    task = find_task_by_id(tasks, task_id)

    if task is None:
        return False

    tasks.remove(task)
    save_tasks(tasks)

    return True