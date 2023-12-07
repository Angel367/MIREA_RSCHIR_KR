from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),

    path('services/', ServiceListView.as_view(), name='service-list'),
    path('services/<int:pk>/', ServiceDetailView.as_view(), name='service-detail'),

    path('specialists/', SpecialistListView.as_view(), name='specialist-list'),
    path('specialists/<int:pk>/', SpecialistDetailView.as_view(), name='specialist-detail'),

    path('cabinets/', CabinetListView.as_view(), name='cabinet-list'),

    path('make_appointment/', make_appointment, name='make-appointment'),

    path('login/', AuthLoginView.as_view(), name='login'),
    path('signup/', RegisterView.as_view(), name='signup'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
