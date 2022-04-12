from django.contrib import admin

from trip_app.accounts.models import Profile, TripAppUser


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(TripAppUser)
class UserAdmin(admin.ModelAdmin):
    filter_horizontal = ("groups", "user_permissions")
