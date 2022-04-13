from django.db import models

# Create your models here.
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32,verbose_name='书名')
    pub_date = models.DateField(verbose_name='出版日期')
    price = models.DecimalField(max_digits=8,decimal_places=2,verbose_name='价格')
    publish = models.CharField(max_length=32,verbose_name='出版社')

    def __str__(self):
        return self.title

