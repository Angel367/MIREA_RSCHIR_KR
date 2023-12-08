from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),

    path('services/', ServiceListView.as_view(), name='service-list'),
    path('services/<int:pk>/', ServiceDetailView.as_view(), name='service-detail'),

    path('specialists/', SpecialistListView.as_view(), name='specialist-list'),
    path('specialists/<int:pk>/', SpecialistDetailView.as_view(), name='specialist-detail'),

    path('make_appointment/', make_appointment, name='make-appointment'),

    path('login/', AuthLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('signup/', RegisterView.as_view(), name='signup'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/edit/', ProfileEditView.as_view(), name='profile_edit'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
