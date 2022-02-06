"""career_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from . import views

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)

urlpatterns = [
    path(r"admin/", admin.site.urls),
    # path(r"api/auth/login/", views.CustomAuthToken.as_view(), name="auth-login"),
    # path(r"api/auth/", include("rest_framework.urls", namespace="rest_framework")),
    path(r"api/auth/login/", TokenObtainPairView.as_view(), name="token-obtain-pair"),
    path(r"api/auth/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
    path(r"api/auth/verify/", TokenVerifyView.as_view(), name="token-verify"),
    path(r"api/auth/me/", views.AuthMe.as_view(), name="auth-login"),
    path(r"api/", views.api_root, name="api-root"),
    path(r"api/", include(router.urls)),
    path(r"api/", include("cv_generator.urls")),
]
