from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registrardocente', views.registrardocente, name='registrardocente'),
    path('registrardicente', views.registrardicente, name='registrardicente'),
    path('resetsenha', views.resetsenha, name='resetsenha'),
    path('login', views.login, name='login'),
]