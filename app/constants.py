from libs.base_enum import BaseEnum


class TaskStatus(BaseEnum):
    ACTIVE = "ACTIVE"
    COMPLETE = "COMPLETE"
    REJECTED_BY_CHILD = "REJECTED_BY_CHILD"
    REJECTED_BY_PARENT = "REJECTED_BY_PARENT"
    PAID = "PAID"

   

