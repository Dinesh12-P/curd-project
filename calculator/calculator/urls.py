from django.urls import path
from . import views

urlpatterns = [
    path('calc', views.calculator_view, name='calculator'),
]
