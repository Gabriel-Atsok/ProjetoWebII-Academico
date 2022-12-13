from django.urls import path
from . import views

urlpatterns = [ 
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('edit_cadastro/', views.edit_cadastro, name='edit_cadastro'),
]
