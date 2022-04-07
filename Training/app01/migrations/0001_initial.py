# Generated by Django 2.2.5 on 2022-04-06 15:19

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('brief', models.CharField(blank=True, max_length=255, null=True)),
                ('content', models.CharField(max_length=255, verbose_name='文章内容')),
                ('pub_date', models.DateTimeField(blank=True, null=True)),
                ('last_modify', models.DateTimeField(auto_now=True)),
                ('priority', models.IntegerField(default=1000, verbose_name='优先级')),
                ('status', models.CharField(choices=[('draft', '草稿'), ('published', '已发布'), ('hidden', '隐藏')], default='published', max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('signature', models.CharField(blank=True, max_length=255, null=True)),
                ('head_img', models.ImageField(blank=True, height_field=150, null=True, upload_to='', width_field=150)),
                ('user', models.OneToOneField(on_delete='CASCADE', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_type', models.IntegerField(choices=[(1, '评论'), (2, '点赞')], default=1)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('article', models.ForeignKey(on_delete='CASCADE', to='app01.Article', verbose_name='所属文章')),
                ('parent_comment', models.ForeignKey(blank=True, null=True, on_delete='CASCADE', related_name='my_children', to='app01.Comment')),
                ('user', models.ForeignKey(on_delete='CASCADE', to='app01.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('brief', models.CharField(blank=True, max_length=255, null=True)),
                ('set_as_top_menu', models.BooleanField(default=False)),
                ('position_index', models.SmallIntegerField()),
                ('admins', models.ManyToManyField(blank=True, to='app01.UserProfile')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete='CASCADE', to='app01.UserProfile'),
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete='CASCADE', to='app01.Category'),
        ),
    ]