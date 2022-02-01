from rest_framework import serializers

from .models import *


class LanguageProficiencySerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = LanguageProficiency
        fields = "__all__"


class WorkTaskTranslationSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = WorkTaskTranslation
        fields = "__all__"


class WorkTaskSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    translations = WorkTaskTranslationSerializer(many=True)

    class Meta:
        model = WorkTask
        fields = "__all__"


class WorkExperienceTranslationSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = WorkExperienceTranslation
        fields = "__all__"


class WorkExperienceSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    translations = WorkExperienceTranslationSerializer(many=True)
    tasks = WorkTaskSerializer(many=True, read_only=True)

    class Meta:
        model = WorkExperience
        fields = "__all__"


class UserProfileTranslationSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = UserProfileTranslation
        fields = "__all__"

class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    user = serializers.HyperlinkedRelatedField(view_name="user-detail", read_only=True)
    translations = UserProfileTranslationSerializer(many=True)
    languages = LanguageProficiencySerializer(many=True, read_only=True)

    class Meta:
        model = UserProfile
        fields = "__all__"


class ProjectTranslationSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = ProjectTranslation
        fields = "__all__"


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    translations = ProjectTranslationSerializer(many=True)
    category = serializers.SlugRelatedField("name", read_only=True)

    class Meta:
        model = Project
        fields = "__all__"


class ProjectCategorySerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    projects = serializers.HyperlinkedRelatedField(many=True, view_name="project-detail", read_only=True)

    class Meta:
        model = ProjectCategory
        fields = "__all__"


class CVTranslationSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = CVTranslation
        fields = "__all__"


class CVSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    translations = CVTranslationSerializer(many=True)
    projects = serializers.HyperlinkedRelatedField(many=True, view_name="project-detail", read_only=True)

    class Meta:
        model = CV
        fields = "__all__"
