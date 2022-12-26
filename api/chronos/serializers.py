from rest_framework import serializers
from .models import Task

from home.serializers import MemberSerializer, HomeSerializer

# Serializers define the API representation.
class TaskSerializer(serializers.ModelSerializer):
    assigned_to = MemberSerializer()
    completed = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = [
            "name",
            "assigned_to",
            "due_date",
            "completed",
        ]

    def get_completed(self, object):
        return object.completed_at != None
