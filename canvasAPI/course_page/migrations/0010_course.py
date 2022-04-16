# Generated by Django 2.2.5 on 2022-04-13 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course_page', '0009_delete_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=32)),
                ('course_code', models.CharField(max_length=16)),
                ('semester', models.CharField(max_length=16)),
                ('course_id', models.CharField(max_length=16)),
            ],
        ),
    ]
