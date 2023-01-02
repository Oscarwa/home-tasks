from datetime import date
from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.decorators import action

from rest_framework.response import Response

from .serializers import GrocerySerializer
from .models import Grocery, GroceryLevel

# Create your views here.
class GroceryViewSet(viewsets.ModelViewSet):
    queryset = Grocery.objects.all()
    serializer_class = GrocerySerializer

    next_status = {
        GroceryLevel.EMPTY: GroceryLevel.FULL,
        GroceryLevel.FULL: GroceryLevel.NORMAL,
        GroceryLevel.NORMAL: GroceryLevel.LOW,
        GroceryLevel.LOW: GroceryLevel.EMPTY,
    }

    def list(self, request, *args, **kwargs):
        member = request.user
        if not member:
            return Response(None)
        list = Grocery.objects.filter(home=member.home)
        serializer = GrocerySerializer(list, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        member = request.user
        serializer = GrocerySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(home=member.home)
            return Response(serializer.data)

    @action(detail=True, methods=["POST"])
    def toggle(self, request, pk=None):
        member = request.user
        grocery = Grocery.objects.get(pk=pk, home=member.home)
        if grocery:
            next = self.next_status[grocery.level]
            grocery.level = next
            grocery.save()
            return Response({"success": True, "new_state": next})
        return Response({"success": False})
