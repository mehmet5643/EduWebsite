# Generated by Django 4.0.3 on 2022-04-23 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionApp', '0006_alter_question_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='answer',
            field=models.CharField(max_length=1, null='A'),
            preserve_default='A',
        ),
    ]
