from django.core.management import BaseCommand
from apps.redirect.models import Redirect
from django.core.cache import cache


class Command(BaseCommand):
    def handle(self, *args, **options):
        active_redirects = list(Redirect.objects.filter(_active=True))

        for redirect in active_redirects:
            key = redirect._key
            data = redirect.get_redirect(key)
            cache.set(key, data)
