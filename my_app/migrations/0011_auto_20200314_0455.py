# Generated by Django 3.0.3 on 2020-03-14 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0010_auto_20200313_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='big_subject',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
