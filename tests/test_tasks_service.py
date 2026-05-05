from uuid import UUID

import pytest

from src.modules.tasks.models import TaskStatus
from src.modules.tasks.service import TaskService, TaskNotFoundError


def test_create_task() -> None:
    service = TaskService()

    task = service.create_task(
        title="Купить молоко",
        description="2 литра",
        status=TaskStatus.NEW,
    )

    assert isinstance(task.id, UUID)
    assert task.title == "Купить молоко"
    assert task.description == "2 литра"
    assert task.status == TaskStatus.NEW


def test_get_task_by_id() -> None:
    service = TaskService()

    created_task = service.create_task(
        title="Купить молоко",
        description=None,
        status=TaskStatus.NEW,
    )

    found_task = service.get_task_by_id(created_task.id)

    assert found_task == created_task


def test_get_unknown_task() -> None:
    service = TaskService()

    with pytest.raises(TaskNotFoundError):
        service.get_task_by_id(
            UUID("00000000-0000-0000-0000-000000000000")
        )
