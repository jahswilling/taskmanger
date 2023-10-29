
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

User = get_user_model()

class Command(BaseCommand):
    help = 'Creates a superuser.'

    def handle(self, *args, **options):
        if not User.objects.filter(email='admin1@gamil.com').exists():
            User.objects.create_superuser(
                email='admin1@gamil.com',
                password='complexpassword123'
            )
        print('Superuser has been created.')