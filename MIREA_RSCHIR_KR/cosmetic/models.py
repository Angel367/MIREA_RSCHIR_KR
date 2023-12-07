from django.contrib.auth.models import AbstractUser
from django.db import models


# Модель Пользователь
class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    is_client = models.BooleanField(default=True)
    is_specialist = models.BooleanField(default=False)
    photo = models.CharField(max_length=100)
    birth_date = models.DateField(null=True)
    groups = None
    user_permissions = None


# Модель Специалист
class Specialist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialty = models.CharField(max_length=100)
    description = models.TextField()


# Модель Категория
class ServiceCategory(models.Model):
    title = models.CharField(max_length=100)


# Модель Услуга
class Service(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)
    description = models.TextField()
    duration = models.DurationField()  # время оказания
    price = models.DecimalField(max_digits=10, decimal_places=2)


# Модель Кабинет
class Cabinet(models.Model):
    number = models.SmallIntegerField()
    specialists = models.ManyToManyField(Specialist)


# Модель Запись
class Appointment(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    specialist = models.ForeignKey(Specialist, on_delete=models.CASCADE)
    cabinet = models.ForeignKey(Cabinet, on_delete=models.SET_NULL, blank=True, null=True)
    datetime = models.DateTimeField()
