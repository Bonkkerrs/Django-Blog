# Generated by Django 2.2.5 on 2022-04-13 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_page', '0003_auto_20220413_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_code',
            field=models.IntegerField(),
        ),
    ]
