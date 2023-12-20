from django.urls import path
from . import views


urlpatterns = [
    path('', views.currencies_view),
    path('commodities/', views.commodities_view, name='commodities_page'),
    path('index_stocks/', views.index_stocks_view, name='index_stocks_page'),

]
