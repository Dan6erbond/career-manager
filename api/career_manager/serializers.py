from cv_generator.models import UserProfile
from cv_generator.serializers import WorkExperienceSerializer
from django.contrib.auth.models import Group, User
from rest_framework import serializers


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = serializers.PrimaryKeyRelatedField(read_only=True)
    work_experiences = serializers.HyperlinkedRelatedField(view_name="workexperience-detail", many=True, read_only=True)

    class Meta:
        model = User
        fields = "__all__"


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"
