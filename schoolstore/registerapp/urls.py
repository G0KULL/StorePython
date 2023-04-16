from django.urls import path,include
from . import views


urlpatterns = [
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('new',views.new,name='new'),
    path('form',views.form,name='form'),
    path('confirmation',views.confirmation,name='confirmation'),
]