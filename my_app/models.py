from django.db import models

# Create your models here.
class One_task(models.Model):
    big_subject = models.CharField(max_length=50)
    task = models.CharField(max_length=50)
    sub_task = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    jindu = models.CharField(max_length=50)

    def __str__(self):
        return str(self.task+":"+self.sub_task)

