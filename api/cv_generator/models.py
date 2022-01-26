from django.db import models

LANGUAGES = [
    ("en", "English"),
    ("de", "German"),
]

LANGUAGE_LEVEL = [
    ("basic", "Basic"),
    ("conversational", "Conversational"),
    ("fluent", "Fluent"),
    ("native", "Native"),
    ("bilingual", "Bilingual"),
]


class UserProfile(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    website = models.URLField(blank=True, null=True)


class UserProfileTranslation(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    language = models.CharField(max_length=2, choices=LANGUAGES)
    headline = models.CharField(max_length=100, blank=True)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)


class LanguageProficiency(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    language = models.CharField(max_length=100, blank=True)
    proficiency = models.CharField(
        choices=LANGUAGE_LEVEL, default="Basic", max_length=100
    )


class CV(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    projects = models.ManyToManyField("Project", through="CVProject")

    class Meta:
        ordering = ["created"]


class CVTranslation(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    language = models.CharField(max_length=2, choices=LANGUAGES)
    headline = models.CharField(max_length=100, blank=True)
    cv = models.ForeignKey(CV, on_delete=models.CASCADE)


class WorkExperience(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    cvs = models.ManyToManyField(CV)
    company = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    class Meta:
        ordering = ["start_date"]


class WorkExperienceTranslation(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    language = models.CharField(max_length=2, choices=LANGUAGES)
    position = models.CharField(max_length=100, blank=True)
    work_experience = models.ForeignKey(WorkExperience, on_delete=models.CASCADE)


class WorkTask(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    work_experience = models.ForeignKey(WorkExperience, on_delete=models.CASCADE)

    class Meta:
        ordering = ["created"]


class WorkTaskTranslation(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    language = models.CharField(max_length=2, choices=LANGUAGES)
    task = models.CharField(max_length=512, blank=True)
    work_task = models.ForeignKey(WorkTask, on_delete=models.CASCADE)


class ProjectCategory(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ["created"]


class Project(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    category = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE)

    class Meta:
        ordering = ["created"]


class ProjectTranslation(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    language = models.CharField(max_length=2, choices=LANGUAGES)
    name = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=512, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class CVProject(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    cv = models.ForeignKey(CV, on_delete=models.CASCADE)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ["order"]
