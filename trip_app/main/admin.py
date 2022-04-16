from django.contrib import admin

from trip_app.main.models import Driver, Vehicle, PopularTrip


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name',)


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    # filter_horizontal = ("groups", "user_permissions")
    pass


@admin.register(PopularTrip)
class PopularTripAdmin(admin.ModelAdmin):
    pass