from datetime import date
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action

from rest_framework.response import Response

from .serializers import TaskSerializer, InternalTaskSerializer
from .models import Task
from home.models import Home

# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_classes = {"create": InternalTaskSerializer}
    # serializer_class = TaskSerializer  # Your default serializer
    default_serializer_class = TaskSerializer  # Your default serializer

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    def create(self, request, *args, **kwargs):
        member = request.user
        serializer = InternalTaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(home=member.home, created_by=member)
            return Response(serializer.data)

    @action(detail=True, methods=["POST"])
    def complete(self, request, pk=None):
        task = Task.objects.get(pk=pk)
        if task.completed_at == None:
            task.completed_at = date.today()
            task.save()
            return Response({"success": True})
        return Response({"success": False})
