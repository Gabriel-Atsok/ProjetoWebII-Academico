from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registrar', views.registrardocente, name='registrar'),
    path('resetsenha', views.resetsenha, name='resetsenha'),
    path('login', views.login, name='login'),
]