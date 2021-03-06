from django.urls import path, reverse_lazy
from django.views.generic import RedirectView

from trip_app.accounts.views import UserRegisterView, EditProfileView, UserLoginView, ProfileDetailsView, \
    UserLogoutView, DeleteProfileView, ChangeUserPasswordView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login user'),
    path('edit-password/', ChangeUserPasswordView.as_view(), name='change password'),
    path('password_change_done/', RedirectView.as_view(url=reverse_lazy('dashboard')), name='password_change_done'),
    path('logout/', UserLogoutView.as_view(), name='logout user'),
    path('profile/edit/<int:pk>/', EditProfileView.as_view(), name='edit profile'),
    path('profile/delete/<int:pk>/', DeleteProfileView.as_view(), name='delete profile'),
    path('profile/details/<int:pk>/', ProfileDetailsView.as_view(), name='profile details'),

]