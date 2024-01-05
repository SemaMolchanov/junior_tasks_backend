from django.contrib import admin
from .models import CategoryModel, TaskModel, PredefinedTaskModel

# Register your models here.

admin.site.register(CategoryModel)
admin.site.register(TaskModel)
admin.site.register(PredefinedTaskModel)