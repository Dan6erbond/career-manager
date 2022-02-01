from rest_framework import generics, permissions, viewsets

from .models import *
from .permissions import IsOwner
from .serializers import *


class UserProfileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]


class CVViewSet(viewsets.ModelViewSet):
    queryset = CV.objects.all()
    serializer_class = CVSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]


class ProjectCategoryList(generics.ListAPIView):
    queryset = ProjectCategory.objects.all()
    serializer_class = ProjectCategorySerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]


class ProjectCategoryDetail(generics.RetrieveAPIView):
    queryset = ProjectCategory.objects.all()
    serializer_class = ProjectCategorySerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]


class ProjectTranslationViewset(viewsets.ReadOnlyModelViewSet):
    queryset = ProjectTranslation.objects.all()
    serializer_class = ProjectTranslationSerializer
    permission_classes = [permissions.IsAuthenticated]


class WorkExperienceViewSet(viewsets.ModelViewSet):
    queryset = WorkExperience.objects.all()
    serializer_class = WorkExperienceSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]


class WorkExperienceTranslationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = WorkExperienceTranslation.objects.all()
    serializer_class = WorkExperienceTranslationSerializer
    permission_classes = [permissions.IsAuthenticated]


class WorkTaskViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = WorkTask.objects.all()
    serializer_class = WorkTaskSerializer
    permission_classes = [permissions.IsAuthenticated]


class WorkTaskTranslationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = WorkTaskTranslation.objects.all()
    serializer_class = WorkTaskTranslationSerializer
    permission_classes = [permissions.IsAuthenticated]
