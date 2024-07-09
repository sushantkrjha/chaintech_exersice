from django.urls import path
from . import views

urlpatterns = [
    path('form/', views.user_form),
    path('data/', views.user_data),
]
