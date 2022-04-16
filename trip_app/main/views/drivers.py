from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views import generic as views

from trip_app.main.forms import CreateDriverForm
from trip_app.main.models import Driver
from django.contrib.auth import mixins as auth_mixin


class DriverDetailsView(auth_mixin.LoginRequiredMixin, views.ListView):
    model = Driver
    template_name = 'main/driver_details.html'
    context_object_name = 'driver'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['drivers'] = Driver.objects.all()

        return context


class CreateDriverView(views.CreateView):
    template_name = 'main/driver_create.html'
    form_class = CreateDriverForm
    success_url = reverse_lazy('driver details')


    # def dispatch(self, request, *args, **kwargs):
    #     if not self.user.has_permission():
    #         pass
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class UserAccessToDriverMixin(PermissionRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not self.user.has_permission():
            pass


class EditDriverView(PermissionRequiredMixin, views.UpdateView):

    permission_required = 'main.driver.change_driver'

    model = Driver
    template_name = 'main/driver_edit.html'
    fields = '__all__'



    def get_success_url(self):
        return reverse_lazy('driver details')


class DeleteDriverView(PermissionRequiredMixin, views.DeleteView):
    permission_required = 'driver.delete_driver'
    model = Driver
    template_name = 'main/driver_delete.html'
    fields = '__all__'
    # form_class = DeleteDriverForm

    def get_success_url(self):
        return reverse_lazy('driver details')