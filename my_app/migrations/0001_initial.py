# Generated by Django 3.0.3 on 2020-03-11 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='One_task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('big_subject', models.CharField(max_length=50)),
                ('task', models.CharField(max_length=50)),
                ('sub_task', models.CharField(max_length=50)),
                ('time', models.DateField(max_length=50)),
                ('jindu', models.CharField(max_length=50)),
            ],
        ),
    ]
