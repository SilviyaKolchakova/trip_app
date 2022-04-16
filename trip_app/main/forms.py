from django import forms

from trip_app.common.helpers import DisabledFieldsFormMixin
from trip_app.main.models import Vehicle, Trip, Driver, PopularTrip


class CreateVehicleForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        # self._init_bootstrap_form_controls()

    def save(self, commit=True):
        # commit false does not persist to database
        # just returns the object to be created
        vehicle = super().save(commit=False)

        vehicle.user = self.user
        if commit:
            vehicle.save()

        return vehicle

    class Meta:
        model = Vehicle
        fields = ('type', 'date_of_registration', 'number_of_seats', 'photo', 'price_per_km')
        # widgets = {
        #     'name': forms.TextInput(
        #         attrs={
        #             'placeholder': 'Enter pet name',
        #         }
        #     ),
        # }


# class EditVehicleForm(forms.ModelForm):
#
#     # def __init__(self, *args, **kwargs):
#     #     super().__init__(*args, **kwargs)
#     #     self._init_bootstrap_form_controls()
#
#     class Meta:
#         model = Vehicle
#         fields = ('type', 'date_of_registration', 'number_of_seats', 'photo', 'price_per_km')
#         # exclude = ('user_profile',)


class DeleteVehicleForm(DisabledFieldsFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self._init_bootstrap_form_controls()
        self._init_disabled_fields()

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Vehicle
        fields = ('type', 'date_of_registration', 'number_of_seats', 'photo', 'price_per_km')
        # exclude = ('user_profile',)


class CreateTripForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        # self._init_bootstrap_form_controls()

    def save(self, commit=True):
        # commit false does not persist to database
        # just returns the object to be created
        trip = super().save(commit=False)

        trip.user = self.user
        if commit:
            trip.save()

        return trip

    class Meta:
        model = Trip
        exclude = ('review', 'user', 'review' )
        # fields = ('start_date', 'end_date', 'starting_point', 'destination', 'distance', 'number_of_passengers', 'vehicle', 'driver')
        widgets = {
            'starting_point': forms.TextInput(
                # attrs={
                #     'placeholder': 'Enter pet name',
                # }
            ), 'destination': forms.TextInput()
        }


class CreateDriverForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        # self._init_bootstrap_form_controls()

    def save(self, commit=True):
        # commit false does not persist to database
        # just returns the object to be created
        driver = super().save(commit=False)

        driver.user = self.user
        if commit:
            driver.save()

        return driver

    class Meta:
        model = Driver
        fields = '__all__'
        # widgets = {
        #     'name': forms.TextInput(
        #         attrs={
        #             'placeholder': 'Enter pet name',
        #         }
        #     ),
        # }


class Popular_trip:
    pass


class CreatePopularTripForm(forms.ModelForm):

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        # self._init_bootstrap_form_controls()

    def save(self, commit=True):
        # commit false does not persist to database
        # just returns the object to be created
        popular_trip = super().save(commit=False)

        popular_trip.user = self.user
        if commit:
            popular_trip.save()

        return popular_trip

    class Meta:
        model = PopularTrip
        fields = ('popular_trip_name', 'popular_trip_photo',)