from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

router = DefaultRouter()
router.register(r"user_profiles", views.UserProfileViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

urlpatterns = format_suffix_patterns(urlpatterns)
