# Generated by Django 2.2.5 on 2022-04-15 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_page', '0012_auto_20220414_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='canvasuseraccount',
            name='canvas_id',
            field=models.CharField(max_length=32, verbose_name='Canvas ID'),
        ),
        migrations.AlterField(
            model_name='canvasuseraccount',
            name='physical_id',
            field=models.CharField(max_length=32, verbose_name='学号/工号'),
        ),
    ]
