# Generated by Django 2.2.5 on 2022-04-13 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_page', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='course_nickname',
        ),
        migrations.AddField(
            model_name='course',
            name='end_year',
            field=models.IntegerField(default=''),
        ),
        migrations.AddField(
            model_name='course',
            name='semester',
            field=models.IntegerField(default=''),
        ),
        migrations.AddField(
            model_name='course',
            name='start_year',
            field=models.IntegerField(default=''),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_code',
            field=models.IntegerField(default=''),
        ),
    ]
