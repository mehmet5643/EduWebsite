# Generated by Django 4.0.3 on 2022-04-24 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionApp', '0016_test_rename_name_categories_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='test',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
