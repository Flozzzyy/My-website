from . import views
from django.urls import path

urlpatterns = [
    path('', views.mainpage, name='home'),
    path('about/', views.about_page, name='about'),
]
