from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # path('contact/', views.contact, name='contact'),
    path('review/', views.review, name='review'),
    path('review/success/', views.review_success, name='review_success'),
]