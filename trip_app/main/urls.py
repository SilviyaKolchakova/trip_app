from django.urls import path

from trip_app.main.views.drivers import CreateDriverView, DriverDetailsView, EditDriverView, DeleteDriverView
from trip_app.main.views.generic import HomeView, DashboardView, AdminView, CreatePopularTripView
from trip_app.main.views.trips import CreateTripView, TripDetailsView, EditTripView, DeleteTripView
from trip_app.main.views.vehicles import CreateVehicleView, EditVehicleView, DeleteVehicleView, VehicleDetailsView

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('adminview/', AdminView.as_view(), name='admin_view'),
    path('popular/add/', CreatePopularTripView.as_view(), name='create popular trip'),

    path('vehicle/add/', CreateVehicleView.as_view(), name='create vehicle'),
    path('vehicle/edit/<int:pk>/', EditVehicleView.as_view(), name='edit vehicle'),
    path('vehicle/delete/<int:pk>/', DeleteVehicleView.as_view(), name='delete vehicle'),
    path('vehicle/details/', VehicleDetailsView.as_view(), name='vehicle details'),

    path('driver/add/', CreateDriverView.as_view(), name='create driver'),
    path('driver/edit/<int:pk>/', EditDriverView.as_view(), name='edit driver'),
    path('driver/delete/<int:pk>/', DeleteDriverView.as_view(), name='delete driver'),
    path('driver/details/', DriverDetailsView.as_view(), name='driver details'),

    path('trip/add/', CreateTripView.as_view(), name='create trip'),
    path('trip/details/<int:pk>/', TripDetailsView.as_view(), name='trip details'),
    path('trip/edit/<int:pk>/', EditTripView.as_view(), name='edit trip'),
    path('trip/delete/<int:pk>/', DeleteTripView.as_view(), name='delete trip'),
]