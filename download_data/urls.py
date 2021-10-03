from . import views
from django.urls import path

urlpatterns = [
    path('<str:tid>',views.ticker, name='ticker'),
    path('', views.index,name = 'index'),
]
