from datetime import datetime
from decimal import Decimal
from PIL import Image
from app.constants import TaskStatus
from dataclasses import dataclass
from typing import List


@dataclass
class CategoryEntity:
    category_id: int
    category_name_en: str
    category_name_ru: str
    category_name_kz: str

@dataclass
class TaskNameEntity:
    task_name_id: int
    name_en: str
    name_kz: str
    name_ru: str
    category_id: int


@dataclass
class GetTaskNamesResponseEntity:
    categories: List[CategoryEntity]
    task_names: List[TaskNameEntity]


@dataclass
class CreateTaskInputEntity:
    name: str
    description: str
    due: datetime
    price: Decimal
    iban: str


@dataclass
class ChangeTaskStatusInputEntity:
    task_id: int
    status: TaskStatus


@dataclass
class GetTaskDetailsInputEntity:
    task_id: int


@dataclass
class GetTaskDetailsResponseEntity:
    name: str
    description: str
    due: datetime
    price: Decimal


@dataclass
class DeleteTaskInputEntity:
    task_id: int


@dataclass
class GetTasksInputEntity:
    iban: str


@dataclass
class GetTasksResponseEntity:
    task_id: int
    name: str
    description: str
    due: datetime
    price: Decimal
    image: Image
    status: TaskStatus
    parent_id: str
    child_id: str
    iban: str


@dataclass
class GetChildIdInputEntity:
    iban: str


@dataclass
class GetChildIdResponseEntity:
    child_id: str


@dataclass
class AddTaskImageInputEntity:
    task_id: int
    image: Image