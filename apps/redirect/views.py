from django.http import JsonResponse
from .models import Redirect
from django.core.cache import cache
from django.db.models import F
# Create your views here.


def RedirectsView(request):
    redirects = list(Redirect.objects.values(
        key=F('_key'), url=F('_url'), active=F('_active')))

    return JsonResponse(redirects, safe=False)


def RedirectView(request, key):
    if cache.get(key):
        redirect = cache.get(key)
        response_data = {'key': key, 'url': redirect['url']}
        return JsonResponse(response_data)
    return JsonResponse({'error': 'no data'})
