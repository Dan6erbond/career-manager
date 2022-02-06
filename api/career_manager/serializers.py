from cv_generator.models import UserProfile
from cv_generator.serializers import WorkExperienceSerializer
from django.contrib.auth.models import Group, User
from rest_framework import serializers


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = serializers.HyperlinkedRelatedField(
        view_name="userprofile-detail", read_only=True
    )
    work_experiences = serializers.HyperlinkedRelatedField(
        view_name="workexperience-detail", many=True, read_only=True
    )

    class Meta:
        model = User
        fields = [
            "url",
            "profile",
            "work_experiences",
            "last_login",
            "is_superuser",
            "username",
            "first_name",
            "last_name",
            "email",
            "is_staff",
            "is_active",
            "date_joined",
            "groups",
            "user_permissions",
        ]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"
