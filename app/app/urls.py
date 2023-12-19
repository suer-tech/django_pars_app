from django.urls import include, path
from .admin import stocks_admin_site

urlpatterns = [
    path('admin/', stocks_admin_site.urls),
    path('', include('stock_parser.urls')),

]
