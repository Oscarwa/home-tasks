from rest_framework import serializers
from .models import Task

from home.serializers import MemberLiteSerializer, HomeSerializer

# Serializers define the API representation.
class TaskSerializer(serializers.ModelSerializer):
    assigned_to = MemberLiteSerializer()
    created_by = MemberLiteSerializer()
    completed = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = [
            "id",
            "name",
            "assigned_to",
            "due_date",
            "completed",
            "created_by",
        ]

    def get_completed(self, object):
        return object.completed_at != None


class InternalTaskSerializer(serializers.ModelSerializer):
    assigned_to_id = serializers.IntegerField()

    class Meta:
        model = Task
        fields = ["name", "assigned_to_id", "due_date"]
