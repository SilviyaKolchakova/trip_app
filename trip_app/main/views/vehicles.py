from django.urls import reverse_lazy
from django.views import generic as views

from trip_app.main.forms import CreateVehicleForm, DeleteVehicleForm
from trip_app.main.models import Vehicle
from django.contrib.auth import mixins as auth_mixin


class VehicleDetailsView(auth_mixin.LoginRequiredMixin, views.ListView):
    model = Vehicle
    template_name = 'main/vehicle_details.html'
    context_object_name = 'vehicle'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['vehicles'] = Vehicle.objects.all()

        return context


class CreateVehicleView(views.CreateView):
    template_name = 'main/vehicle_create.html'
    form_class = CreateVehicleForm
    success_url = reverse_lazy('dashboard')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class EditVehicleView(views.UpdateView):
    model = Vehicle
    template_name = 'main/vehicle_edit.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('vehicle details')


class DeleteVehicleView(views.DeleteView):
    model = Vehicle
    template_name = 'main/vehicle_delete.html'
    form_class = DeleteVehicleForm
    success_url = reverse_lazy('dashboard')