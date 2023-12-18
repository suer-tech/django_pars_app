from django.urls import path
from .admin import stocks_admin_site


urlpatterns = [
    path('admin/', stocks_admin_site.urls),

]
