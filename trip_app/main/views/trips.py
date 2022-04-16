from datetime import date

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views import generic as views

from trip_app.common.helpers import get_driver_payment
from trip_app.main.forms import CreateTripForm
from trip_app.main.models import Trip
from django.contrib.auth import mixins as auth_mixin, get_user

driver_cost_per_day = 40


class TripDetailsView(auth_mixin.LoginRequiredMixin, views.DetailView):
    model = Trip
    template_name = 'main/trip_details.html'
    context_object_name = 'trip'

    # def get_queryset(self):
    #     return super() \
    #         .get_queryset() \
    #         .prefetch_related('review')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        trip_days = (self.object.end_date - self.object.start_date).days
        driver_payment = get_driver_payment(trip_days, driver_cost_per_day)
        trip_cost = self.object.distance * self.object.vehicle.price_per_km
        total_trip_cost = driver_payment + trip_cost
        days_before_trip = (self.object.start_date - date.today()).days

        context['is_owner'] = self.object.user == self.request.user
        context['driver_payment'] = driver_payment
        context['trip_cost'] = trip_cost
        context['total_trip_cost'] = total_trip_cost
        context['days_before_trip'] = days_before_trip
        # context['is_superuser'] = self.request.user == self.request.user.is_superuser()

        return context


class CreateTripView(auth_mixin.LoginRequiredMixin, views.CreateView):
    template_name = 'main/trip_create.html'
    form_class = CreateTripForm
    success_url = reverse_lazy('dashboard')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditTripView(views.UpdateView):
    model = Trip
    template_name = 'main/trip_edit.html'
    fields = ('start_date', 'end_date', 'starting_point', 'destination', 'distance', 'vehicle', 'driver')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['is_owner'] = self.object.user == self.request.user

        return context

    def get_success_url(self):
        return reverse_lazy('trip details', kwargs={'pk': self.object.id})


class DeleteTripView(views.DeleteView):
    model = Trip
    template_name = 'main/trip_delete.html'
    fields = '__all__'
    # form_class = DeletePetForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['is_owner'] = self.object.user == self.request.user

        return context

    def get_success_url(self):
        return reverse_lazy('dashboard')