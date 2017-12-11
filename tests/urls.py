from django.conf import settings
from django.conf.urls import url
from .views import return_404, error_500

urlpatterns = [
    url(r'^404$', return_404, name='test'),
    url(r'^500$', error_500, name='test'),
]
