from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexPage, name='index'),
    path('about/', AboutPage, name='about'),
    path('api/', ApiPage, name='api'),
    path('contact/', ContactPage, name='contact'),
]