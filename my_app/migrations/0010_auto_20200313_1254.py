# Generated by Django 3.0.3 on 2020-03-13 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0009_auto_20200313_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='big_subject',
            name='name',
            field=models.CharField(choices=[(1, '管理工作'), (2, '后装工作'), (3, '政治工作')], max_length=50),
        ),
    ]