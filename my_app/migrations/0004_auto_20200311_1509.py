# Generated by Django 3.0.3 on 2020-03-11 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0003_auto_20200311_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='one_task',
            name='time',
            field=models.CharField(max_length=50),
        ),
    ]