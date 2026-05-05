from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status

from src.modules.tasks.dependencies import get_task_service
from src.modules.tasks.exceptions import TaskNotFoundError
from src.modules.tasks.schemas import CreateTask, TaskResponse
from src.modules.tasks.service import TaskService


router = APIRouter(prefix='/tasks', tags=['tasks'])

@router.post(
    '',
    response_model=TaskResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_task(
    task: CreateTask,
    task_service: TaskService = Depends(get_task_service),
) -> TaskResponse:
    created_task = task_service.create_task(**task.model_dump())
    return TaskResponse.model_validate(created_task)

@router.get(
    '',
    response_model=list[TaskResponse],
    status_code=status.HTTP_200_OK,
)
def get_tasks(
    task_service: TaskService = Depends(get_task_service),
) -> list[TaskResponse]:
    tasks = task_service.get_tasks()
    return [TaskResponse.model_validate(task) for task in tasks]

@router.get(
    '/{task_id}',
    response_model=TaskResponse,
)
def get_task(
    task_id: UUID,
    task_service: TaskService = Depends(get_task_service)
) -> TaskResponse:
    try:
        task = task_service.get_task_by_id(task_id)
    except TaskNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Задача не найдена",
        ) from exc

    return TaskResponse.model_validate(task)