from typing import Optional
from uuid import UUID, uuid4

from src.modules.tasks.models import Task, TaskStatus


class TaskNotFoundError(Exception):
    pass

class TaskService:
    def __init__(self) -> None:
        self._tasks: dict[UUID, Task] = {}

    def create_task(self, title: str, description: Optional[str], status: TaskStatus) -> Task:
        task = Task(
            id=uuid4(),
            title=title,
            description=description,
            status=status,
        )

        self._tasks[task.id] = task
        return task

    def get_tasks(self) -> list[Task]:
        return [task for task in self._tasks.values()]

    def get_task_by_id(self, task_id: UUID) -> Task:
        task = self._tasks.get(task_id)
        if task is None:
            raise TaskNotFoundError
        return task
