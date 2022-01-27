# Generated by Django 4.0.1 on 2022-01-26 22:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cv_generator', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cv',
            name='headline',
        ),
        migrations.RemoveField(
            model_name='project',
            name='description',
        ),
        migrations.RemoveField(
            model_name='project',
            name='name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='headline',
        ),
        migrations.RemoveField(
            model_name='workexperience',
            name='position',
        ),
        migrations.RemoveField(
            model_name='worktask',
            name='task',
        ),
        migrations.CreateModel(
            name='WorkTaskTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('language', models.CharField(choices=[('en', 'English'), ('de', 'German')], max_length=2)),
                ('task', models.CharField(blank=True, max_length=512)),
                ('work_task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cv_generator.worktask')),
            ],
        ),
        migrations.CreateModel(
            name='WorkExperienceTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('language', models.CharField(choices=[('en', 'English'), ('de', 'German')], max_length=2)),
                ('position', models.CharField(blank=True, max_length=100)),
                ('work_experience', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cv_generator.workexperience')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfileTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('language', models.CharField(choices=[('en', 'English'), ('de', 'German')], max_length=2)),
                ('headline', models.CharField(blank=True, max_length=100)),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cv_generator.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('language', models.CharField(choices=[('en', 'English'), ('de', 'German')], max_length=2)),
                ('name', models.CharField(blank=True, max_length=100)),
                ('description', models.CharField(blank=True, max_length=512)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cv_generator.project')),
            ],
        ),
        migrations.CreateModel(
            name='CVTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('language', models.CharField(choices=[('en', 'English'), ('de', 'German')], max_length=2)),
                ('headline', models.CharField(blank=True, max_length=100)),
                ('cv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cv_generator.cv')),
            ],
        ),
    ]