from app.models import (
    CategoryModel,
    TaskModel,
    PredefinedTaskModel
)
from app.entities.entities import (
    CategoryEntity,
    TaskNameEntity,
    GetTaskNamesResponseEntity,
    CreateTaskInputEntity,
    ChangeTaskStatusInputEntity,
    GetTaskDetailsInputEntity,
    GetTaskDetailsResponseEntity,
    DeleteTaskInputEntity,
    GetTasksInputEntity,
    GetTasksResponseEntity,
    GetChildIdInputEntity,
    GetChildIdResponseEntity,
    AddTaskImageInputEntity
)
from app.constants import TaskStatus
from django.conf import settings
import requests
import json


class AppHandler:
    def __init__(self, client_id):
        self.client_id = client_id


    def get_task_names(self) -> GetTaskNamesResponseEntity:

        category_entities = []
        task_name_entities = []

        categories = CategoryModel.objects.all()
        task_names = PredefinedTaskModel.objects.all()
       

        for category in categories:
            category_entity = CategoryEntity(
                category_id=category.id,
                category_name_en=category.category_name_en,
                category_name_kz=category.category_name_kz,
                category_name_ru=category.category_name_ru
            )
            category_entities.append(category_entity)

        for task_name in task_names:
            task_name_entity = TaskNameEntity(
                task_name_id=task_name.id,
                name_en=task_name.name_en,
                name_kz=task_name.name_kz,
                name_ru=task_name.name_ru,
                category_id=task_name.category_id
            )
            task_name_entities.append(task_name_entity)

        
        
        created_task_names = TaskModel.objects.filter(
            parent_id=self.client_id).values_list('name', flat=True)

        for created_task_name in created_task_names:
            task_name_entity = TaskNameEntity(
                task_name_id=None,
                name_en=created_task_name,
                name_kz=created_task_name,
                name_ru=created_task_name,
                category_id=None
            )
            task_name_entities.append(task_name_entity)

        return GetTaskNamesResponseEntity(
            categories=category_entities,
            task_names=task_name_entities
        )

    def create_task(self, input_entity: CreateTaskInputEntity) -> TaskModel:

        client_id_child = self.get_child_id(input_entity)

        task_model = TaskModel(
            name=input_entity.name,
            description=input_entity.description,
            due=input_entity.due,
            price=input_entity.price,
            status=TaskStatus.ACTIVE.value,
            parent_id=self.client_id,
            child_id=client_id_child,
            iban=input_entity.iban
        )
        
        task_model.save()
        return task_model
    

    def change_task_status(self, input_entity: ChangeTaskStatusInputEntity):
        task = TaskModel.objects.get(id=input_entity.task_id) 
        task.status = input_entity.status
        task.save()

        

    def get_task_details(self, 
                         input_entity: GetTaskDetailsInputEntity) -> GetTaskDetailsResponseEntity:
        response_entity = TaskModel.objects.get(id=input_entity.task_id)
        

        return GetTaskDetailsResponseEntity(
            name=response_entity.name,
            description=response_entity.description,
            due=response_entity.due,
            price=response_entity.price
        )


    def delete_task(self, input_entity: DeleteTaskInputEntity):
        record = TaskModel.objects.get(id=input_entity.task_id)

        if record.parent_id == self.client_id:
            record.delete()


    def get_tasks_parent(self, input_entity: GetTasksInputEntity):
        task_entities = []
        tasks = TaskModel.objects.filter(parent_id=self.client_id, iban=input_entity.iban)
        
        for task in tasks:
            task_entity = GetTasksResponseEntity(
                task_id=task.id,
                name=task.name,
                description=task.description,
                due=task.due,
                price=task.price,
                image=task.image,
                status=task.status,
                parent_id=task.parent_id,
                child_id=task.child_id,
                iban=task.iban
            )
            task_entities.append(task_entity)

        return task_entities
    

    def get_tasks_child(self):
        task_entities = []
        tasks = TaskModel.objects.filter(child_id=self.client_id)
        
        for task in tasks:
            task_entity = GetTasksResponseEntity(
                task_id=task.id,
                name=task.name,
                description=task.description,
                due=task.due,
                price=task.price,
                image=task.image,
                status=task.status,
                parent_id=task.parent_id,
                child_id=task.child_id,
                iban=task.iban
            )
            task_entities.append(task_entity)

        return task_entities
    

    def get_child_id(self, 
                         input_entity: GetChildIdInputEntity
                         ) -> str:
        
        URL = settings.DOMAIN + '/proxy/cards-service/srv/cards/get_client_child_info'
        print(URL)

        payload = {}

        payload["client_id"] = self.client_id
        payload["iban"] = input_entity.iban

        headers = {"x-access-token": settings.X_ACCESS_TOKEN}

        print(payload)
        print(headers)


        response = requests.get(URL, params=payload, headers=headers).json()

        print(response)

        client_id_child = response['data']['client_id']

        return client_id_child
    


    def add_task_image(self, input_entity: AddTaskImageInputEntity):
        task = TaskModel.objects.get(id=input_entity.task_id)
        task.image = input_entity.image
        task.save()