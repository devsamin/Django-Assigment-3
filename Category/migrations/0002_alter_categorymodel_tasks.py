# Generated by Django 5.1.2 on 2024-10-24 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Category', '0001_initial'),
        ('Task', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorymodel',
            name='Tasks',
            field=models.ManyToManyField(related_name='categories', to='Task.taskmodel'),
        ),
    ]
