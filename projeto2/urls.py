from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('cadpessoas.urls')), # inclui as rotas do app 'cadpessoas' sob o prefixo /api/
]
