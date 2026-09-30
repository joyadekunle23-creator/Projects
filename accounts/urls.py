from django.urls import path
from .views import register, login_view, dashboard, savings_goals

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('dashboard/',dashboard, name='dashboard'),
    path('savings-goals/', savings_goals, name='savings_goals'),
]
