from django.urls import path
from .views import RedirectView, RedirectsView

urlpatterns = [
    path('', RedirectsView),
    path('<str:key>', RedirectView)
]
