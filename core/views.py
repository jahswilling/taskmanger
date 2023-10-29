from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import *
from datetime import datetime

from .serializers import *
# Create your views here.

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

channel_layer = get_channel_layer()

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """Retrieve the tasks for the authenticated user"""
        return self.queryset.filter(assigned_to=self.request.user)

    def perform_create(self, serializer):
        """Create a new task for the authenticated user"""
        serializer.save(author=self.request.user)

    # You can override other methods like update, retrieve, destroy, etc., as needed.

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # Add custom logic here if needed, such as logging the update action.

        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        # Add custom logic here, such as tracking when a task is viewed.

        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)

        # Add custom logic here, such as sending notifications before deletion.

        return Response(status=status.HTTP_204_NO_CONTENT)
    



@async_to_sync
async def send_real_time_update(task_id, message):
    await channel_layer.group_send(f'task_{task_id}', {
        'type': 'task_status.update',
        'message': message
    })
