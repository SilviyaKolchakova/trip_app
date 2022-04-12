import datetime


from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth import forms

from trip_app.common.validators import validate_only_letters

UserModel = get_user_model()


class Vehicle(models.Model):
    SEDAN = 'sedan'
    COUPE = "coupe"
    SUV = 'suv'
    HATCHBACK = 'hatchback'
    JEEP = 'jeep'
    MINIVAN = 'minivan'
    VAN = 'van'
    BUS = "bus"

    TYPES = [(x, x) for x in (SEDAN, COUPE,SUV, HATCHBACK, JEEP, MINIVAN, VAN, BUS)]

    TWO = 2
    FOUR = 4
    FIVE = 5
    SEVEN = 7
    EIGHT = 8
    FIFTEEN = 15
    TWENTY = 20

    SEATS = [(x, x) for x in (TWO, FOUR, FIVE, SEVEN, EIGHT, FIFTEEN, TWENTY)]
    NUMBER_OF_SEATS_MAX_LENGTH = 2

    type = models.CharField(
        max_length=max(len(x) for (x, _) in TYPES),
        choices=TYPES,
    )

    date_of_registration = models.DateField(
        null=True,
        blank=True,
        validators=(
            # MinDateValidator(),
        )
    )

    number_of_seats = models.IntegerField(
        # max_length=NUMBER_OF_SEATS_MAX_LENGTH,
        choices=SEATS,
    )

    photo = models.ImageField(
        validators=(
            # validate_file_max_size_in_mb(5),
            # validate_file_max_size_in_mb(7),
            # validate_file_max_size_in_mb(8),

        ),upload_to='vehicles',
    )

    price_per_km = models.DecimalField(
        max_digits=6,
        decimal_places=2)

    def __str__(self):
        return f'{self.type}'


class Driver(models.Model):
    FIRST_NAME_MIN_LENGTH = 2
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 30

    CATEGORY_B = 'B'
    CATEGORY_D = 'D'

    LICENSE_CATEGORY = [(x, x) for x in (CATEGORY_B, CATEGORY_D)]

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            validate_only_letters,
        )
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
            validate_only_letters,
        )
    )

    picture = models.ImageField(
        validators=(
            # validate_file_max_size_in_mb(5),
            # validate_file_max_size_in_mb(7),
            # validate_file_max_size_in_mb(8),
        ), upload_to='drivers',
    )

    license_category = models.CharField(
        max_length=max(len(x) for (x, _) in LICENSE_CATEGORY),
        choices=LICENSE_CATEGORY,
    )

    license_receipt_date = models.DateField(
        null=True,
        blank=True,
    )

    @property
    def years_experience(self):
        return datetime.datetime.now().year - self.license_receipt_date.year

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Review(models.Model):
    TITLE_MAX_LENGTH = 30
    DESCRIPTION_MAX_LENGTH = 300

    TERRIBLE = 'terrible'
    POOR = 'poor'
    AVERAGE = 'average'
    GOOD = 'good'
    EXCELLENT = 'excellent'

    TRIP_RATE = [(x, x) for x in (TERRIBLE, POOR, AVERAGE, GOOD, EXCELLENT)]

    title = models.TextField(
        max_length=TITLE_MAX_LENGTH,
        null=True,
        blank=True,
    )

    description = models.TextField(
        max_length=DESCRIPTION_MAX_LENGTH,
        null=True,
        blank=True,
    )

    trip_photo = models.URLField(
        validators=(
            # validate_file_max_size_in_mb(5),
            # validate_file_max_size_in_mb(7),
            # validate_file_max_size_in_mb(8),
        )
    )

    trip_rate = models.CharField(
        max_length=max(len(x) for (x, _) in TRIP_RATE),
        choices=TRIP_RATE,
    )

    publication_date = models.DateTimeField(
        auto_now_add=True,
    )


class Trip(models.Model):
    STARTING_POINT_MAX_LENGTH = 30
    STARTING_POINT_MIN_LENGTH = 3

    DESTINATION_MAX_LENGTH = 30
    DESTINATION_MIN_LENGTH = 3

    start_date = models.DateField(
        null=True,
        blank=True,
        validators=(
            # MinDateValidator(),
        )
    )

    end_date = models.DateField(
        null=True,
        blank=True,
        validators=(
            # MinDateValidator(),
        )
    )

    starting_point = models.CharField(
        max_length=STARTING_POINT_MAX_LENGTH,
        validators=(
            MinLengthValidator(STARTING_POINT_MIN_LENGTH),
            validate_only_letters,
        )
    )

    destination = models.CharField(
        max_length=DESTINATION_MAX_LENGTH,
        validators=(
            MinLengthValidator(DESTINATION_MIN_LENGTH),
            validate_only_letters,
        )
    )

    distance = models.IntegerField(
        default=0,
    )

    number_of_passengers = models.IntegerField(
        choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15),]
    )

    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.PROTECT,

    )

    driver = models.ForeignKey(
        Driver,
        on_delete=models.CASCADE,
    )

    publication_date = models.DateField(
        auto_now_add=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )


class TripPhoto(models.Model):
    photo = models.URLField(
        validators=(
            # validate_file_max_size_in_mb(5),
            # validate_file_max_size_in_mb(7),
            # validate_file_max_size_in_mb(8),
        )
    )
    description = models.TextField(
        null=True,
        blank=True,
    )

    publication_date = models.DateField(
        auto_now_add=True,
    )

    tagged_trip = models.ManyToManyField(
        Trip,
        # validate at least 1 pet
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )


class PopularTrip(models.Model):
    TRIP_NAME_MAX_LENGTH = 100

    popular_trip_name = models.TextField(
        max_length=TRIP_NAME_MAX_LENGTH
    )

    popular_trip_photo = models.ImageField(
        validators=(
            # validate_file_max_size_in_mb(5),
            # validate_file_max_size_in_mb(7),
            # validate_file_max_size_in_mb(8),
        ), upload_to='popular_trips',
    )