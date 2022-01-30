from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

router = DefaultRouter()
router.register(r"user_profiles", views.UserProfileViewSet)
router.register(r"cvs", views.CVViewSet)
router.register(r"projects", views.ProjectViewSet)
router.register(r"project_translations", views.ProjectTranslationViewset)

urlpatterns = [
    path("project_categories/", views.ProjectCategoryList.as_view(), name="projectcategory-list"),
    path("project_categories/<int:pk>/", views.ProjectCategoryDetail.as_view(), name="projectcategory-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += router.urls
