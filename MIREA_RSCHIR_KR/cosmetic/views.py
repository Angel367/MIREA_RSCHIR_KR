# Импорты моделей
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, ListView, DetailView
from .forms import AppointmentForm, RegisterForm
from .models import *
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy


class AuthLoginView(LoginView):
    template_name = 'login.html'
    extra_context = {'title': 'Вход'}


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ProfileView(DetailView):
    model = User
    template_name = 'profile.html'

    def get_object(self, **kwargs):
        return self.request.user


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавление данных
        return context


class AboutView(TemplateView):
    template_name = "about.html"

    extra_context = {"specialists": Specialist.objects.all()}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ServiceListView(ListView):
    model = Service
    template_name = "service_list.html"

    extra_context = {"categories": ServiceCategory.objects.all()}


class ServiceDetailView(DetailView):
    model = Service
    template_name = "service_detail.html"


class SpecialistListView(ListView):
    extra_context = {"specialists": Specialist.objects.all()}
    model = Specialist
    template_name = "specialist_list.html"


class SpecialistDetailView(DetailView):
    model = Specialist
    template_name = "specialist_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # можно добавить доп данные по специалисту
        return context


class CabinetListView(ListView):
    model = Cabinet
    template_name = "main/cabinet_list.html"


def make_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            service = form.cleaned_data['service']
            specialist = form.cleaned_data['specialist']
            date = form.cleaned_data['date']
            client = request.user

            # Создаем и сохраняем запись
            appointment = Appointment(
                client=client,
                service=service,
                specialist=specialist,
                datetime=date
            )
            appointment.save()

            return redirect('appointment-confirmation')
        else:
            form = AppointmentForm()

        return render(request, 'main/make_appointment.html', {'form': form})
