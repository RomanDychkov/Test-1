from django.urls import path
from . import views
urlpatterns = [
    path('', views.test),
    path('about', views.about),
    path('hope', views.hope)


    ]