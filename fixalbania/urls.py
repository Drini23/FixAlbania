from django.urls import path
from fixalbania import views


urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('about_us/', views.about_us, name='about_us'),
    path('contact/', views.contact, name='contact'),
]