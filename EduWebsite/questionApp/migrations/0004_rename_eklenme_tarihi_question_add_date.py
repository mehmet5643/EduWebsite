# Generated by Django 4.0.3 on 2022-04-23 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionApp', '0003_alter_question_options_question_admin_verified'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='eklenme_tarihi',
            new_name='add_date',
        ),
    ]