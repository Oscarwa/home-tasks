from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Member, Home
from .serializers import MemberHomeSerializer, HomeSerializer

# Create your views here.
class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberHomeSerializer

    def list(self, request, *args, **kwargs):
        member = request.user
        members = Member.objects.filter(home=member.home)
        serializer = MemberHomeSerializer(members, many=True)
        return Response(serializer.data)


class HomeViewSet(viewsets.ModelViewSet):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer

    def list(self, request, *args, **kwargs):
        member = request.user
        home = Home.objects.get(pk=member.home.id)
        serializer = HomeSerializer(home)
        return Response(serializer.data)
