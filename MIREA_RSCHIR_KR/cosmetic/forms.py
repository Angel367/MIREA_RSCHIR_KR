from .models import Service, Specialist, User
from django import forms
from django.contrib.auth.forms import UserCreationForm


class AppointmentForm(forms.Form):

    service = forms.ModelChoiceField(
        queryset=Service.objects.all(),
        label='Услуга'
    )
    specialist = forms.ModelChoiceField(
        queryset=Specialist.objects.all(),
        label='Специалист'
    )

    date = forms.DateTimeField(
        label='Дата и время',
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
    )

    class Meta:
        fields = [
            'service',
            'specialist',
            'date'
        ]


class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        label='Email',
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )

    username = forms.CharField(
        label='Имя пользователя',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    password2 = forms.CharField(
        label='Подтверждение пароля',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = [
            'email',
            'username',
            'password1',
            'password2'
        ]
