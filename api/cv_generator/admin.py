from django.contrib import admin

from .models import (
    CV,
    CVProject,
    LanguageProficiency,
    Project,
    UserProfile,
    WorkExperience,
    WorkTask,
)


class LanguageProficiencyInline(admin.TabularInline):
    model = LanguageProficiency
    extra = 1


class UserProfileAdmin(admin.ModelAdmin):
    inlines = [LanguageProficiencyInline]


admin.site.register(UserProfile, UserProfileAdmin)


class WorkTaskInline(admin.TabularInline):
    model = WorkTask
    extra = 1


class WorkExperienceAdmin(admin.ModelAdmin):
    inlines = [WorkTaskInline]


admin.site.register(WorkExperience, WorkExperienceAdmin)

admin.site.register(Project)


class CVProjectInline(admin.TabularInline):
    model = CVProject
    extra = 1


class CVAdmin(admin.ModelAdmin):
    inlines = [CVProjectInline]


admin.site.register(CV, CVAdmin)
