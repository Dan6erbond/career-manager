from rest_framework import serializers

from .models import *


class LanguageProficiencySerializer(serializers.ModelSerializer):
    class Meta:
        model = LanguageProficiency
        fields = ["created", "language", "proficiency"]


class WorkTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkTask
        fields = ["created", "task"]


class WorkExperienceSerializer(serializers.ModelSerializer):
    tasks = WorkTaskSerializer(many=True, read_only=True)

    class Meta:
        model = WorkExperience
        fields = ["created", "company", "position", "start_date", "end_date", "tasks"]


class UserProfileSerializer(serializers.ModelSerializer):
    languages = LanguageProficiencySerializer(many=True, read_only=True)
    work_experiences = WorkExperienceSerializer(many=True, read_only=True)

    class Meta:
        model = UserProfile
        fields = [
            "created",
            "user",
            "headline",
            "email",
            "phone",
            "website",
            "languages",
            "work_experiences",
        ]


class ProjectSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField("name", read_only=True)

    class Meta:
        model = Project
        fields = ["created", "name", "description", "category"]


class ProjectCategorySerializer(serializers.ModelSerializer):
    projects = ProjectSerializer(many=True, read_only=True)

    class Meta:
        model = ProjectCategory
        fields = ["created", "name", "projects"]


class CVSerializer(serializers.ModelSerializer):
    projects = ProjectSerializer(many=True, read_only=True)

    class Meta:
        model = CV
        fields = ["id", "created", "headline", "projects"]
