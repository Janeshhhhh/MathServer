from django.contrib import admin
from django.urls import path
from mojang import views

urlpatterns = [
    path('', views.churn_calculator, name='churn_calculator'),
]