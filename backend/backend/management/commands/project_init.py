from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
from app_assignments.models import Assignment, Hint
from django.contrib.sites.models import Site
import os

class Command(BaseCommand):
    help = 'Init project on the first run'

    def handle(self, *args, **options):
        self.stdout.write('Starting project_init...')

        #creating a super user, if doesn't exists
        User = get_user_model()
        if len(User.objects.filter(is_superuser=True)) == 0:
            User.objects.create_superuser(password='qweqwe111', username='admin')
            self.stdout.write('Superuser created.')

        # setting a domain name to Site and populating DB
        try:
            site = Site.objects.get(domain='example.com')
            site.domain = os.environ.get("DOMAIN")
            site.name = os.environ.get("DOMAIN")
            site.save()
            self.stdout.write('Site edited - domain is set.')

            for i in range(15):
                assignment_description = 'Text description for assignment {}'.format(i)
                instance = Assignment.objects.create(description=assignment_description)

                hint_description= 'Text description for hint #1 for assignment {}'.format(i)
                Hint.objects.create(
                    description=hint_description,
                    assignment=instance
                )

                hint_description= 'Text description for hint #2 for assignment {}'.format(i)
                Hint.objects.create(
                    description=hint_description,
                    assignment=instance
                )


        except Exception:
            pass
        
        self.stdout.write('Project_init finished.')