# Generated by Django 5.1.2 on 2024-10-24 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Category', '0003_remove_categorymodel_tasks'),
        ('Task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskmodel',
            name='categories',
            field=models.ManyToManyField(to='Category.categorymodel'),
        ),
    ]
