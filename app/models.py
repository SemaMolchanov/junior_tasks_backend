from django.db import models
from model_utils.models import TimeStampedModel
from app.constants import TaskStatus

# Create your models here.

class CategoryModel(TimeStampedModel):
    category_name_en = models.TextField()
    category_name_kz = models.TextField()
    category_name_ru = models.TextField()

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class TaskModel(TimeStampedModel):
    name = models.TextField()
    description = models.TextField()
    due = models.DateTimeField()
    price = models.DecimalField(max_digits=9, decimal_places=2)
    image = models.ImageField()
    status = models.CharField(max_length=32,
                              choices=TaskStatus.choices(),
                              default=TaskStatus.ACTIVE)
    parent_id = models.CharField(max_length=32, db_index=True)
    child_id = models.CharField(max_length=32, db_index=True)
    iban = models.CharField(max_length=32, db_index=True)

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"


class PredefinedTaskModel(TimeStampedModel):
    name_en = models.TextField()
    name_kz = models.TextField()
    name_ru = models.TextField()
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Predefined Task"
        verbose_name_plural = "Predefined Tasks"