# Generated by Django 3.2 on 2023-10-10 16:17

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('study', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='lessonviesinfo',
            unique_together={('lesson', 'user')},
        ),
    ]
