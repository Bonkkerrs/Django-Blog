# Generated by Django 2.2.5 on 2022-04-06 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_article_head_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='head_img',
            field=models.ImageField(upload_to='uploads/pics', verbose_name='文章标题图片'),
        ),
    ]