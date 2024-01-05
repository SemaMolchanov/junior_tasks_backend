from rest_framework import serializers
from app.constants import TaskStatus
from libs.base_serializer import (
    BaseSerializer,
    EnumField
)
from app.entities.entities import (
    CreateTaskInputEntity,
    ChangeTaskStatusInputEntity,
    GetTaskDetailsInputEntity,
    GetTaskDetailsResponseEntity,
    DeleteTaskInputEntity,
    GetTasksInputEntity,
    GetTasksResponseEntity,
    GetChildIdInputEntity,
    AddTaskImageInputEntity
)



class CategorySerializer(BaseSerializer):
    category_id = serializers.IntegerField()
    category_name_en = serializers.CharField()
    category_name_kz = serializers.CharField()
    category_name_ru = serializers.CharField()



class TaskNameSerializer(BaseSerializer):
    task_name_id = serializers.IntegerField()
    name_en = serializers.CharField()
    name_kz = serializers.CharField()
    name_ru = serializers.CharField()
    category_id = serializers.IntegerField()



class GetTaskNamesResponseSerializer(BaseSerializer):
    categories = serializers.ListSerializer(child=CategorySerializer())
    task_names = serializers.ListSerializer(child=TaskNameSerializer())



class CreateTaskInputSerializer(BaseSerializer):
    name = serializers.CharField()
    description = serializers.CharField()
    due = serializers.DateTimeField()
    price = serializers.DecimalField(max_digits=9, decimal_places=2)
    iban = serializers.CharField()

    def create(self, validated_data):
        return CreateTaskInputEntity(**validated_data)
    


class ChangeTaskStatusInputSerializer(BaseSerializer):
    task_id = serializers.IntegerField()
    status = serializers.ChoiceField(choices=TaskStatus.choices())

    def create(self, validated_data):
        return ChangeTaskStatusInputEntity(**validated_data)
    


class GetTaskDetailsInputSerializer(BaseSerializer):
    task_id = serializers.IntegerField()

    def create(self, validated_data):
        return GetTaskDetailsInputEntity(**validated_data)



class GetTaskDetailsResponseSerializer(BaseSerializer):
    name = serializers.CharField()
    description = serializers.CharField()
    due = serializers.DateTimeField()
    price = serializers.DecimalField(max_digits=9, decimal_places=2)




class DeleteTaskInputSerializer(BaseSerializer):
    task_id = serializers.IntegerField()

    def create(self, validated_data):
        return DeleteTaskInputEntity(**validated_data)
    

class GetTasksInputSerializer(BaseSerializer):
    iban = serializers.CharField()

    def create(self, validated_data):
        return GetTasksInputEntity(**validated_data)
    

class GetTasksResponseSerializer(BaseSerializer):
    task_id = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()
    due = serializers.DateTimeField()
    price = serializers.DecimalField(max_digits=9, decimal_places=2)
    image = serializers.ImageField()
    status = serializers.ChoiceField(choices=TaskStatus.choices())
    parent_id = serializers.CharField()
    child_id = serializers.CharField()
    iban = serializers.CharField()


class GetChildIdInputSerializer(BaseSerializer):
    iban = serializers.CharField()

    def create(self, validated_data):
        return GetChildIdInputEntity(**validated_data)
    

class GetChildIdResponseSerializer(BaseSerializer):
    child_id = serializers.CharField()
    

class AddTaskImageInputSerializer(BaseSerializer):
    task_id = serializers.IntegerField()
    image = serializers.ImageField()

    def create(self, validated_data):
        return AddTaskImageInputEntity(**validated_data)