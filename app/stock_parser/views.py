from django.shortcuts import render
from .models import Stocks


def index(request):
    template = 'stock_parser/index.html'
    stock_list = Stocks.objects.all()
    context = {"stock_list": stock_list}
    return render(request, template, context)



