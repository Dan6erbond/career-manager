from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path("user-profiles/", views.UserProfileList.as_view()),
    path("user-profiles/<int:pk>", views.UserProfileDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
