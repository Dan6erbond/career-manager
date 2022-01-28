from django import forms
from django.contrib.admin.decorators import display
from django.contrib import admin

import nested_admin

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


class EducationTaskTranslationForm(forms.ModelForm):
    task = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = EducationTaskTranslation
        fields = "__all__"


class EducationTaskTranslationInline(nested_admin.NestedTabularInline):
    model = EducationTaskTranslation
    extra = 0
    form = EducationTaskTranslationForm


class EducationTaskAdmin(admin.ModelAdmin):
    inlines = [EducationTaskTranslationInline]
    list_display = ["get_user", "education"]
    list_filter = ["education__user"]

    @display(description="User")
    def get_user(self, obj: EducationTask):
        return obj.education.user


admin.site.register(EducationTask, EducationTaskAdmin)


class EducationTaskInline(nested_admin.NestedStackedInline):
    model = EducationTask
    inlines = [EducationTaskTranslationInline]
    extra = 0


class EducationTranslationInline(nested_admin.NestedTabularInline):
    model = EducationTranslation
    extra = 0


class EducationAdmin(nested_admin.NestedModelAdmin):
    inlines = [EducationTranslationInline, EducationTaskInline]
    list_display = ["user", "institution", "start_date", "end_date"]
    list_filter = ["user"]


admin.site.register(Education, EducationAdmin)


class WorkTaskTranslationForm(forms.ModelForm):
    task = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = WorkTaskTranslation
        fields = "__all__"


class WorkTaskTranslationInline(nested_admin.NestedTabularInline):
    model = WorkTaskTranslation
    extra = 0
    form = WorkTaskTranslationForm


class WorkTaskAdmin(admin.ModelAdmin):
    model = WorkTask
    inlines = [WorkTaskTranslationInline]


admin.site.register(WorkTask, WorkTaskAdmin)


class WorkTaskInline(nested_admin.NestedTabularInline):
    model = WorkTask
    extra = 1
    inlines = [WorkTaskTranslationInline]


class WorkExperienceTranslationInline(nested_admin.NestedTabularInline):
    model = WorkExperienceTranslation
    extra = 1


class WorkExperienceAdmin(nested_admin.NestedModelAdmin):
    inlines = [WorkTaskInline, WorkExperienceTranslationInline]
    list_display = ["user", "company"]
    list_filter = ["user"]


admin.site.register(WorkExperience, WorkExperienceAdmin)


class ProjectTranslationForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = ProjectTranslation
        fields = "__all__"


class ProjectTranslationInline(nested_admin.NestedStackedInline):
    form = ProjectTranslationForm
    model = ProjectTranslation
    extra = 0


class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectTranslationInline]
    list_display = ["user", "category", "name"]
    list_filter = ["user", "category"]


admin.site.register(Project, ProjectAdmin)


class ProjectInline(nested_admin.NestedTabularInline):
    model = Project
    inlines = [ProjectTranslationInline]
    extra = 0


class ProjectCategoryAdmin(nested_admin.NestedModelAdmin):
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
