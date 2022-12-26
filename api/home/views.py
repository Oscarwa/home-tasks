from django.shortcuts import render
from rest_framework import viewsets

from .models import Member, Home
from .serializers import MemberSerializer, HomeSerializer

# Create your views here.
class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class HomeViewSet(viewsets.ModelViewSet):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer
