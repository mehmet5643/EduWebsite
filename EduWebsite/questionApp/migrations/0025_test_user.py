# Generated by Django 4.0.3 on 2022-05-12 16:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questionApp', '0024_remove_question_test_alter_test_questions'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='user',
            field=models.ManyToManyField(blank=True, related_name='Test_joined', to=settings.AUTH_USER_MODEL),
        ),
    ]
