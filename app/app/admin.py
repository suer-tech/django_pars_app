import sys

from django.contrib import admin
from stock_parser.admin import StocksAdmin
from stock_parser.models import Stocks

sys.path.append("..")
class StocksAdminSite(admin.AdminSite):
    site_header = 'Stocks Admin'
    site_title = 'Stocks Admin'


stocks_admin_site = StocksAdminSite(name='stocks_admin')
stocks_admin_site.register(Stocks, StocksAdmin)
