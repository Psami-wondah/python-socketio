# Generated by Django 4.0.1 on 2022-01-10 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_io', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='short_id',
            field=models.CharField(default='09MCV8R2B', max_length=255),
        ),
    ]