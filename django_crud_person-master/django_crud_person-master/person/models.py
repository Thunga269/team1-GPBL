from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(verbose_name='Name', max_length=255)
    age = models.PositiveIntegerField(verbose_name='Age')
    address = models.CharField(verbose_name='Address', max_length=255)
    phone_number = models.CharField(verbose_name='Phone number', max_length=20)
    email = models.EmailField(verbose_name='Email', max_length=255)
    id_company = models.CharField(verbose_name='Company code', max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        __tablename__ = 'Person'
        #ordering = ['created_at'] -> sorting