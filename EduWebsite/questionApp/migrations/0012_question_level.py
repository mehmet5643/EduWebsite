# Generated by Django 4.0.3 on 2022-04-24 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionApp', '0011_alter_question_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='level',
            field=models.PositiveIntegerField(default=5, max_length=5, null=2),
            preserve_default=2,
        ),
    ]