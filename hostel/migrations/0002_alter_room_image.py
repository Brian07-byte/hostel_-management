# Generated by Django 5.1.1 on 2024-09-13 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='image',
            field=models.ImageField(upload_to='room_image/'),
        ),
    ]
