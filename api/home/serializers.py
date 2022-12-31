from rest_framework import serializers
from .models import Member, Home

# Serializers define the API representation.
class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ["id", "name", "email", "last_login", "phone_number", "updated_at"]


class MemberLiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ["id", "name"]


class HomeSerializer(serializers.ModelSerializer):
    admin = MemberSerializer()

    class Meta:
        model = Home
        fields = ["id", "name", "admin"]


class MemberHomeSerializer(serializers.ModelSerializer):
    home = HomeSerializer()

    class Meta:
        model = Member
        fields = [
            "id",
            "name",
            "email",
            "last_login",
            "phone_number",
            "updated_at",
            "home",
        ]
