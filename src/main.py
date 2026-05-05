import logging
from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI

from src.modules.tasks.api import router as tasks_router
from src.modules.tasks.service import TaskService


logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    app.state.task_service = TaskService()
    logger.info("TaskService initialized")

    yield

    logger.info("Application shutdown")

app = FastAPI(
    title="Task Scheduler API",
    lifespan=lifespan,
)
app.include_router(tasks_router)
