from django.urls import path
from .views import vitima_list
from .views import vitimas_new
from .views import vitima_dados
from .views import vitima_delete

urlpatterns = [
    path ('', vitimas_new, name = 'vitimas_new'),
    path ('list/',vitima_list, name ='vitima_list'),
    path ('dados/<int:id>/',vitima_dados, name='vitima_dados'),
    path ('delete/<int:id>/',vitima_delete, name='vitima_delete'),
]