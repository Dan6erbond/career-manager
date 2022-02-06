from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

router = DefaultRouter()
router.register(r"user_profiles", views.UserProfileViewSet)
router.register(r"cvs", views.CVViewSet)
router.register(r"projects", views.ProjectViewSet)
router.register(r"project_translations", views.ProjectTranslationViewset)
router.register(r"work_experiences", views.WorkExperienceViewSet)
router.register(r"work_experience_translations", views.WorkExperienceTranslationViewSet)
router.register(r"work_tasks", views.WorkTaskViewSet)
router.register(r"work_task_translations", views.WorkTaskTranslationViewSet)

urlpatterns = [
    path(
        r"project_categories/",
        views.ProjectCategoryList.as_view(),
        name="projectcategory-list",
    ),
    path(
        r"project_categories/<int:pk>/",
        views.ProjectCategoryDetail.as_view(),
        name="projectcategory-detail",
    ),
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += router.urls
