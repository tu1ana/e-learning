from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='mod@example.com',
            # first_name='Admin',
            # last_name='Adminski',
            is_superuser=False,
            is_staff=True,
            is_active=True
        )
        user.set_password('123asd456asd')
        user.save()
