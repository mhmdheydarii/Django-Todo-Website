from django.core.management.base import BaseCommand
from faker import Faker
from django.contrib.auth.models import User
from todo.models import Task
from datetime import datetime


class Command(BaseCommand):
    help = 'Generate test data using Faker'
    
    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.fake = Faker()

    def handle(self, *args, **kwargs):
        user = User.objects.create(
            username = self.fake.name(),
            last_name = self.fake.last_name(),
            first_name = self.fake.first_name(),
            email = self.fake.email(),
            password = "!@#$5678"
        )


        for _ in range(12):
            Task.objects.create(
                author = user,
                task = self.fake.text(),
                start_date = datetime.now(),
            )
