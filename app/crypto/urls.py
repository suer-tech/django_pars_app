from django.urls import path
from . import views


urlpatterns = [
    path('crypto/', views.crypto_page, name='crypto_page'),

]
