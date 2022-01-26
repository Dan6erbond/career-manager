from rest_framework import serializers

from .models import *


class LanguageProficiencySerializer(serializers.ModelSerializer):
    class Meta:
        model = LanguageProficiency
        fields = "__all__"


class WorkTaskTranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkTaskTranslation
        fields = "__all__"


class WorkTaskSerializer(serializers.ModelSerializer):
    translations = WorkTaskTranslationSerializer(many=True)

    class Meta:
        model = WorkTask
        fields = "__all__"


class WorkExperienceTranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExperienceTranslation
        fields = "__all__"


class WorkExperienceSerializer(serializers.ModelSerializer):
    translations = WorkExperienceTranslationSerializer(many=True)
    tasks = WorkTaskSerializer(many=True, read_only=True)

    class Meta:
        model = WorkExperience
        fields = "__all__"


class UserProfileTranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfileTranslation
        fields = "__all__"

class UserProfileSerializer(serializers.ModelSerializer):
    translations = UserProfileTranslationSerializer(many=True)
    languages = LanguageProficiencySerializer(many=True, read_only=True)
    work_experiences = WorkExperienceSerializer(many=True, read_only=True)

    class Meta:
        model = UserProfile
        fields = "__all__"


class ProjectTranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectTranslation
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    translations = ProjectTranslationSerializer(many=True)
    category = serializers.SlugRelatedField("name", read_only=True)

    class Meta:
        model = Project
        fields = "__all__"


class ProjectCategorySerializer(serializers.ModelSerializer):
    projects = ProjectSerializer(many=True, read_only=True)

    class Meta:
        model = ProjectCategory
        fields = "__all__"


class CVTranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CVTranslation
        fields = "__all__"


class CVSerializer(serializers.ModelSerializer):
    translations = CVTranslationSerializer(many=True)
    projects = ProjectSerializer(many=True, read_only=True)

    class Meta:
        model = CV
        fields = "__all__"
