from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

CustomUser = get_user_model()

class Command(BaseCommand):
    help = 'Create a superuser with the office_head role'

    def add_arguments(self, parser):
        parser.add_argument('email', type=str, help='Superuser email address')
        parser.add_argument('password', type=str, help='Superuser password')

    def handle(self, *args, **options):
        email = options['email']
        password = options['password']

        try:
            user = CustomUser.objects.get(email=email)
            self.stdout.write(self.style.ERROR(f'The user with email {email} already exists.'))
        except CustomUser.DoesNotExist:
            user = CustomUser.objects.create_superuser(email=email, password=password, role='office_head')
            self.stdout.write(self.style.SUCCESS(f'Successfully created superuser with email {user.email} and role {user.role}.'))
