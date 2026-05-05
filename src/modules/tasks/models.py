from enum import Enum
from typing import Optional
from uuid import UUID

from pydantic import BaseModel



class TaskStatus(str, Enum):
    NEW = "NEW"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"

class Task(BaseModel):
    id: UUID
    title: str
    description: Optional[str] = None
    status: TaskStatus