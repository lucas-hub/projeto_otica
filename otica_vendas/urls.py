from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', include('clientes.urls')),  # Isso inclui as URLs definidas em clientes/urls.py
]
