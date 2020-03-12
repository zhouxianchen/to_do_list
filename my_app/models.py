from django.db import models

# Create your models here.
class One_task(models.Model):
    BIG_CHOICES = (
        ('FR', 'Freshman'),
        ('SO', 'Sophomore'),
        ('JR', 'Junior'),
        ('SR', 'Senior'),
        ('GR', 'Graduate'),
    )
    big_subject = models.CharField(max_length=50, choices=BIG_CHOICES)
    task = models.CharField(max_length=50)
    sub_task = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    jindu = models.CharField(max_length=50)