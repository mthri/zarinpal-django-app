from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('pay', views.pay),
    path('verify', views.verify),
    path('transactions', views.transactions)
]