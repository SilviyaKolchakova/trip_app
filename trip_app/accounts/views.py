from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, login

from trip_app.accounts.forms import CreateProfileForm

# to check in petstagram - RedirectToDashboard next to views.CreateView
from trip_app.accounts.models import Profile, TripAppUser


class UserRegisterView(views.CreateView):
    form_class = CreateProfileForm
    template_name = 'accounts/profile_create.html'
    success_url = reverse_lazy('dashboard')


class UserLoginView(auth_views.LoginView):
    template_name = 'accounts/login_page.html'
    success_url = reverse_lazy('dashboard')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class EditProfileView(views.UpdateView):
    fields = ('first_name', 'last_name')
    model = Profile
    template_name = 'accounts/edit_profile.html'
    success_url = reverse_lazy('login user')


class DeleteProfileView(views.DeleteView):
    fields = '__all__'
    model = Profile
    template_name = 'accounts/delete_profile.html'
    success_url = reverse_lazy('login user')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.object.user

        return context


class ProfileDetailsView(views.DetailView):
    model = Profile
    template_name = 'accounts/profile_details.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.object.user
        context['is_owner'] = self.request.user == self.object.user

        return context


class UserLogoutView(auth_views.LogoutView):
    template_name = 'accounts/logout_page.html'



