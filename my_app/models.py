from django.db import models

# Create your models here.
# class One_task(models.Model):
#     BIG_CHOICES = (
#         ('FR', 'Freshman'),
#         ('SO', 'Sophomore'),
#         ('JR', 'Junior'),
#         ('SR', 'Senior'),
#         ('GR', 'Graduate'),
#     )
#     big_subject = models.CharField(max_length=50, choices=BIG_CHOICES)
#     task = models.CharField(max_length=50)
#     sub_task = models.CharField(max_length=50)
#     time = models.CharField(max_length=50)
#     jindu = models.CharField(max_length=50)


class Big_subject(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=50)
    big_subject = models.ForeignKey(to='Big_subject', on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.name


class Activity(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    task = models.ForeignKey(to='Task', on_delete=models.CASCADE)
    progress = models.CharField(max_length=50)
    start_time = models.DateField(max_length=50, blank=True)
    end_time = models.DateField(max_length=50, blank=True)

    def __str__(self):
        return self.name


