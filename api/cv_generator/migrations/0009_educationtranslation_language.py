# Generated by Django 4.0.1 on 2022-01-28 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv_generator', '0008_remove_educationtranslation_end_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='educationtranslation',
            name='language',
            field=models.CharField(choices=[('en', 'English'), ('de', 'German')], default='en', max_length=2),
            preserve_default=False,
        ),
    ]
