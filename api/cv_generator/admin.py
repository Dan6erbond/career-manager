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


class WorkTaskInline(admin.TabularInline):
    model = WorkTask
    extra = 1
    inlines = [WorkTaskTranslationInline]


class WorkExperienceTranslationInline(admin.TabularInline):
    model = WorkExperienceTranslation
    extra = 1


class WorkExperienceAdmin(admin.ModelAdmin):
    inlines = [WorkTaskInline, WorkExperienceTranslationInline]


admin.site.register(WorkExperience, WorkExperienceAdmin)


class ProjectTranslationInline(admin.TabularInline):
    model = ProjectTranslation
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectTranslationInline]


admin.site.register(Project, ProjectAdmin)


class ProjectInline(admin.TabularInline):
    model = Project
    extra = 1
    inlines = [ProjectTranslationInline]


class ProjectCategoryAdmin(admin.ModelAdmin):
    inlines = [ProjectInline]


admin.site.register(ProjectCategory, ProjectCategoryAdmin)


class CVProjectInline(admin.TabularInline):
    model = CVProject
    extra = 1


class CVTranslationInline(admin.TabularInline):
    model = CVTranslation
    extra = 1


class CVAdmin(admin.ModelAdmin):
    inlines = [CVTranslationInline, CVProjectInline]


admin.site.register(CV, CVAdmin)
