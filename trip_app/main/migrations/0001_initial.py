# Generated by Django 3.2.12 on 2022-04-13 11:09

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import trip_app.common.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2), trip_app.common.validators.validate_only_letters])),
                ('last_name', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2), trip_app.common.validators.validate_only_letters])),
                ('picture', models.ImageField(upload_to='drivers')),
                ('license_category', models.CharField(choices=[('B', 'B'), ('D', 'D')], max_length=1)),
                ('license_receipt_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PopularTrip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('popular_trip_name', models.TextField(max_length=100)),
                ('popular_trip_photo', models.ImageField(upload_to='popular_trips')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, max_length=30, null=True)),
                ('description', models.TextField(blank=True, max_length=300, null=True)),
                ('trip_photo', models.URLField()),
                ('trip_rate', models.CharField(choices=[('terrible', 'terrible'), ('poor', 'poor'), ('average', 'average'), ('good', 'good'), ('excellent', 'excellent')], max_length=9)),
                ('publication_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('starting_point', models.TextField(max_length=30, validators=[django.core.validators.MinLengthValidator(3), trip_app.common.validators.validate_only_letters])),
                ('destination', models.TextField(max_length=30, validators=[django.core.validators.MinLengthValidator(3), trip_app.common.validators.validate_only_letters])),
                ('distance', models.IntegerField(default=0, validators=[trip_app.common.validators.validate_min_distance])),
                ('number_of_passengers', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15)])),
                ('publication_date', models.DateField(auto_now_add=True)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.driver')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('sedan', 'sedan'), ('coupe', 'coupe'), ('suv', 'suv'), ('hatchback', 'hatchback'), ('jeep', 'jeep'), ('minivan', 'minivan'), ('van', 'van'), ('bus', 'bus')], max_length=9)),
                ('date_of_registration', models.DateField(blank=True, null=True)),
                ('number_of_seats', models.IntegerField(choices=[(2, 2), (4, 4), (5, 5), (7, 7), (8, 8), (15, 15), (20, 20)])),
                ('photo', models.ImageField(upload_to='vehicles')),
                ('price_per_km', models.DecimalField(decimal_places=2, max_digits=6, validators=[trip_app.common.validators.validate_min_price_per_km])),
            ],
        ),
        migrations.CreateModel(
            name='TripPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.URLField()),
                ('description', models.TextField(blank=True, null=True)),
                ('publication_date', models.DateField(auto_now_add=True)),
                ('tagged_trip', models.ManyToManyField(to='main.Trip')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='trip',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.vehicle'),
        ),
    ]
