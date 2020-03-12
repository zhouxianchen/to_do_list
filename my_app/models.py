from django.db import models


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

