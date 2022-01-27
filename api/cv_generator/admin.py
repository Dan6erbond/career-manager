from django import forms
from django.contrib import admin

from .models import *


class LanguageProficiencyInline(admin.TabularInline):
    model = LanguageProficiency
    extra = 1


class UserProfileTranslationInline(admin.TabularInline):
    model = UserProfileTranslation
    extra = 1


class UserProfileAdmin(admin.ModelAdmin):
    inlines = [LanguageProficiencyInline, UserProfileTranslationInline]


admin.site.register(UserProfile, UserProfileAdmin)


class WorkTaskTranslationInline(admin.TabularInline):
    model = WorkTaskTranslation
    extra = 1


class WorkTaskAdmin(admin.ModelAdmin):
    model = WorkTask
    inlines = [WorkTaskTranslationInline]


admin.site.register(WorkTask, WorkTaskAdmin)


class WorkTaskInline(admin.TabularInline):
    model = WorkTask
    extra = 1


class WorkExperienceTranslationInline(admin.TabularInline):
    model = WorkExperienceTranslation
    extra = 1


class WorkExperienceAdmin(admin.ModelAdmin):
    inlines = [WorkTaskInline, WorkExperienceTranslationInline]
    list_display = ["user", "company"]
    list_filter = ["user"]


admin.site.register(WorkExperience, WorkExperienceAdmin)


class ProjectTranslationForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = ProjectTranslation
        fields = "__all__"


class ProjectTranslationInline(admin.StackedInline):
    form = ProjectTranslationForm
    model = ProjectTranslation
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectTranslationInline]
    list_display = ["user", "category", "name"]
    list_filter = ["user", "category"]


admin.site.register(Project, ProjectAdmin)


class ProjectInline(admin.TabularInline):
    model = Project
    extra = 1


class ProjectCategoryAdmin(admin.ModelAdmin):
    inlines = [ProjectInline]
    list_display = ["user", "name"]
    list_filter = ["user"]


admin.site.register(ProjectCategory, ProjectCategoryAdmin)


class CVProjectInline(admin.TabularInline):
    model = CVProject
    extra = 1


class CVTranslationInline(admin.TabularInline):
    model = CVTranslation
    extra = 1


class CVAdmin(admin.ModelAdmin):
    inlines = [CVTranslationInline, CVProjectInline]
    list_display = ["user", "title"]
    list_filter = ["user"]


admin.site.register(CV, CVAdmin)
