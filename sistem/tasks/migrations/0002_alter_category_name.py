# Generated by Django 5.1.4 on 2024-12-22 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(blank=True, default='cualquiera', max_length=100, null=True),
        ),
    ]
