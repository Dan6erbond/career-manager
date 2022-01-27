from rest_framework import serializers

from .models import *


class LanguageProficiencySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LanguageProficiency
        fields = "__all__"


class WorkTaskTranslationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WorkTaskTranslation
        fields = "__all__"


class WorkTaskSerializer(serializers.HyperlinkedModelSerializer):
    translations = WorkTaskTranslationSerializer(many=True)

    class Meta:
        model = WorkTask
        fields = "__all__"


class WorkExperienceTranslationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WorkExperienceTranslation
        fields = "__all__"


class WorkExperienceSerializer(serializers.HyperlinkedModelSerializer):
    translations = WorkExperienceTranslationSerializer(many=True)
    tasks = WorkTaskSerializer(many=True, read_only=True)

    class Meta:
        model = WorkExperience
        fields = "__all__"


class UserProfileTranslationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfileTranslation
        fields = "__all__"

class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(view_name="user-detail", read_only=True)
    translations = UserProfileTranslationSerializer(many=True)
    languages = LanguageProficiencySerializer(many=True, read_only=True)

    class Meta:
        model = UserProfile
        fields = "__all__"


class ProjectTranslationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProjectTranslation
        fields = "__all__"


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    translations = ProjectTranslationSerializer(many=True)
    category = serializers.SlugRelatedField("name", read_only=True)

    class Meta:
        model = Project
        fields = "__all__"


class ProjectCategorySerializer(serializers.HyperlinkedModelSerializer):
    projects = serializers.HyperlinkedRelatedField(many=True, view_name="project-detail", read_only=True)

    class Meta:
        model = ProjectCategory
        fields = "__all__"


class CVTranslationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CVTranslation
        fields = "__all__"


class CVSerializer(serializers.HyperlinkedModelSerializer):
    translations = CVTranslationSerializer(many=True)
    projects = serializers.HyperlinkedRelatedField(many=True, view_name="project-detail", read_only=True)

    class Meta:
        model = CV
        fields = "__all__"
