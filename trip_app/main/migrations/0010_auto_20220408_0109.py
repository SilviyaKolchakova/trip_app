# Generated by Django 3.2.12 on 2022-04-07 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_trip_number_of_passengers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='picture',
            field=models.ImageField(upload_to='drivers'),
        ),
        migrations.AlterField(
            model_name='review',
            name='trip_photo',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='tripphoto',
            name='photo',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='photo',
            field=models.ImageField(upload_to='vehicles'),
        ),
    ]