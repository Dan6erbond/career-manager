from cv_generator.models import UserProfile
from django.contrib.auth.models import Group, User
from rest_framework import serializers

from cv_generator.serializers import WorkExperienceSerializer


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = serializers.PrimaryKeyRelatedField(queryset=UserProfile.objects.all())
    work_experiences = WorkExperienceSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = "__all__"


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"
