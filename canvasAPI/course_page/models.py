from django.db import models

# Create your models here.

class Course(models.Model):
    course_name = models.CharField(max_length=32,verbose_name='课程名称')
    course_code = models.CharField(max_length=16,verbose_name='课程代码')
    semester = models.CharField(max_length=16,blank=False,verbose_name='学期')
    course_id = models.CharField(max_length=16,verbose_name='课程ID')

    def __str__(self):
        return self.course_name

class CanvasUserAccount(models.Model):
    canvas_id = models.CharField(max_length=32,verbose_name='Canvas ID')
    name = models.CharField(max_length=32, verbose_name='姓名')
    physical_id = models.CharField(max_length=32, verbose_name='学号/工号')
    origin = models.ForeignKey('Course',on_delete=models.PROTECT,null=True)

    def __str__(self):
        return self.name
