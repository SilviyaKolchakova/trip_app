import pandas as pd
from datetime import datetime

from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as views

from trip_app.accounts.models import Profile
from trip_app.main.forms import CreatePopularTripForm
from trip_app.main.models import Trip, Review, PopularTrip
from django.contrib.auth import mixins as auth_mixin


class HomeView(views.TemplateView):
    model = PopularTrip
    template_name = 'main/home_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['popular_trips'] = PopularTrip.objects.all()
        context['hide_additional_nav_items'] = True
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')

        return super().dispatch(request, *args, **kwargs)


class DashboardView(auth_mixin.LoginRequiredMixin, views.ListView):
    model = Trip
    template_name = 'main/dashboard.html'
    context_object_name = 'user'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # self.object is a Profile instance
        # context['user'] = self.request.user

        context['trips'] = Trip.objects.all()

        context.update({
            'trips': Trip.objects.all(),
        })

        return context


class AdminView(auth_mixin.LoginRequiredMixin, views.ListView):
    model = Trip
    template_name = 'main/admin.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # self.object is a Profile instance
        # context['user'] = self.request.user

        context['trips'] = Trip.objects.all()

        context.update({
            'trips': Trip.objects.all(),
        })

        return context

class CreatePopularTripView(auth_mixin.LoginRequiredMixin, views.CreateView):
    model = PopularTrip
    form_class = CreatePopularTripForm
    template_name = 'main/popular_trip_create.html'
    success_url = reverse_lazy('admin_view')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

