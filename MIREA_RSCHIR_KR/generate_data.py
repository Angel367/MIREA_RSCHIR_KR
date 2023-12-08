import random
from faker import Faker
from django.utils import timezone
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'MIREA_RSCHIR_KR.settings')  # Замените 'your_project.settings' на путь к вашим настройкам Django
django.setup()

fake = Faker()
User = get_user_model()
from cosmetic.models import Specialist, ServiceCategory, Service, Appointment


class Command(BaseCommand):
    help = 'Generate random data for testing'

    def handle(self, *args, **kwargs):
        # Generate Users
        users = []
        for _ in range(10):
            user = User.objects.create(
                username=fake.user_name(),
                email=fake.email(),
                photo=fake.image_url()
            )
            user.set_password('password123')  # Set a default password for testing
            user.save()
            users.append(user)

        specialists = []
        for _ in range(5):
            specialist_user = User.objects.create(
                username=fake.user_name(),
                email=fake.email(),
                phone=fake.phone_number(),
                photo=fake.image_url(),
                is_client=False,
                is_specialist=True,
            )
            specialist_user.set_password('password123')
            specialist_user.save()

            specialist = Specialist.objects.create(
                user=specialist_user,
                specialty=fake.job(),
                description=fake.text()
            )
            specialists.append(specialist)

        # Generate Service Categories
        categories = []
        for _ in range(5):
            category = ServiceCategory.objects.create(
                title=fake.word(),
            )
            categories.append(category)

        # Generate Services
        services = []
        for _ in range(10):
            service = Service.objects.create(
                title=fake.word(),
                category=random.choice(categories),
                description=fake.text(),
                duration=timezone.timedelta(minutes=random.randint(30, 240)),
                price=random.uniform(10.0, 200.0),
            )
            services.append(service)

        # Generate Appointments
        for _ in range(10):
            appointment = Appointment.objects.create(
                client=random.choice(users),
                service=random.choice(services),
                specialist=random.choice(specialists),
                datetime=fake.future_datetime(),
            )


c = Command()
c.handle()
