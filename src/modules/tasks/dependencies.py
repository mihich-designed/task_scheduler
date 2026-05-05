from fastapi import Request

from src.modules.tasks.service import TaskService


def get_task_service(request: Request) -> TaskService:
    return request.app.state.task_service