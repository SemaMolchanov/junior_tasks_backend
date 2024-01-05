from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from app.serializers.serializers import (
    GetTaskNamesResponseSerializer,
    CreateTaskInputSerializer,
    ChangeTaskStatusInputSerializer,
    GetTaskDetailsInputSerializer,
    GetTaskDetailsResponseSerializer,
    DeleteTaskInputSerializer,
    GetTasksInputSerializer,
    GetTasksResponseSerializer,
    GetChildIdInputSerializer,
    GetChildIdResponseSerializer,
    AddTaskImageInputSerializer
)

from app.handlers.handlers import AppHandler
from libs.middleware.custom_auth import BankingAuthentication


class AppViewSet(viewsets.GenericViewSet):
    authentication_classes = (BankingAuthentication,)


    @action(methods=['get'], detail=False)
    def get_task_names(self, request):
        client_id = request.user.id
        response_entity = AppHandler(client_id=client_id).get_task_names()

        return Response(
            GetTaskNamesResponseSerializer(response_entity).data,
            status=status.HTTP_200_OK
        )


    @action(methods=['post'], detail=False)
    def create_task(self, request):
        client_id = request.user.id

        serializer = CreateTaskInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        input_entity = serializer.save()
        AppHandler(client_id=client_id).create_task(input_entity)

        return Response(status=status.HTTP_201_CREATED)
    

    @action(methods=['put'], detail=False)
    def change_task_status(self, request):
        client_id = request.user.id

        serializer = ChangeTaskStatusInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        input_entity = serializer.save()
        AppHandler(client_id=client_id).change_task_status(input_entity)

        return Response(status=status.HTTP_200_OK)
    


    @action(methods=['get'], detail=False)
    def get_task_details(self, request):
        client_id = request.user.id

        serializer = GetTaskDetailsInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        input_entity = serializer.save()
        response_entity = AppHandler(client_id=client_id).get_task_details(input_entity)

        return Response(
            GetTaskDetailsResponseSerializer(response_entity).data,
            status=status.HTTP_200_OK
        )
    
    @action(methods=['delete'], detail=False)
    def delete_task(self, request):
        client_id = request.user.id

        serializer = DeleteTaskInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        input_entity = serializer.save()
        AppHandler(client_id=client_id).delete_task(input_entity)

        return Response(
            status=status.HTTP_200_OK
        )
    

    @action(methods=['get'], detail=False)
    def get_tasks_parent(self, request):
        client_id = request.user.id

        serializer = GetTasksInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        input_entity = serializer.save()
        response_entity = AppHandler(client_id=client_id).get_tasks_parent(input_entity)

        return Response(
            GetTasksResponseSerializer(response_entity, many=True).data,
            status=status.HTTP_200_OK
        )
    

    @action(methods=['get'], detail=False)
    def get_tasks_child(self, request):
        client_id = request.user.id

    
        response_entity = AppHandler(client_id=client_id).get_tasks_child()

        return Response(
            GetTasksResponseSerializer(response_entity, many=True).data,
            status=status.HTTP_200_OK
        )
    
    @action(methods=['get'], detail=False)
    def get_child_id(self, request):
        client_id = request.user.id

        serializer = GetChildIdInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        input_entity = serializer.save()
        response_entity = AppHandler(client_id=client_id).get_child_id(input_entity)

        return Response(
            response_entity,
            status=status.HTTP_200_OK
        )
    
    @action(methods=['put'], detail=False)
    def add_task_image(self, request):
        client_id = request.user.id

        serializer = AddTaskImageInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        input_entity = serializer.save()
        AppHandler(client_id=client_id).add_task_image(input_entity)

        return Response(status=status.HTTP_200_OK)