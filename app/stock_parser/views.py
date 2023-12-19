from django.shortcuts import render
from .models import Stocks


def index(request, category):
    template = 'stock_parser/index.html'
    stock_list = Stocks.objects.filter(category=category)
    context = {"stock_list": stock_list, "category": category}
    return render(request, template, context)


def currencies_view(request):
    return index(request, category='Валюты')


def commodities_view(request):
    return index(request, category='Товары')


def index_stocks_view(request):
    return index(request, category='Индексы')
