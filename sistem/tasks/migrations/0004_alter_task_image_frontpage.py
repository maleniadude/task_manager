# Generated by Django 5.1.4 on 2024-12-24 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_task_content_task_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='image_frontpage',
            field=models.ImageField(blank=True, default='static/images/image_default.jpg', null=True, upload_to='static/images/'),
        ),
    ]
