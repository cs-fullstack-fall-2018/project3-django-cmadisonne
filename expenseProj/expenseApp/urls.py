from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('setup/', views.setup, name='setup'),
    path('signup/', views.signup, name='signup'),
    path('transaction/<int:pk>', views.transaction, name='transaction'),
    path('emergency/transaction/', views.emergencyTransaction, name='emergencyTransaction'),
]