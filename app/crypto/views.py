from django.shortcuts import render
from .models import Crypto


def crypto_page(request):
    template = 'crypto/crypto.html'
    crypto_top = Crypto.objects.filter(category='top')
    crypto_gainers = Crypto.objects.filter(category='Лидеры роста')
    crypto_loosers = Crypto.objects.filter(category='Лидеры падения')

    context = {
        "crypto_top": crypto_top,
        'crypto_gainers': crypto_gainers,
        'crypto_loosers': crypto_loosers,
        }
    return render(request, template, context)

