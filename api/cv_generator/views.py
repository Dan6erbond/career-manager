from rest_framework import generics, permissions, viewsets

from .models import CV, Project, ProjectCategory, ProjectTranslation, UserProfile
from .permissions import IsOwner
from .serializers import (
    CVSerializer,
    ProjectCategorySerializer,
    ProjectSerializer,
    ProjectTranslationSerializer,
    UserProfileSerializer,
)


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


class ProjectTranslationViewset(viewsets.ModelViewSet):
    queryset = ProjectTranslation.objects.all()
    serializer_class = ProjectTranslationSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]
