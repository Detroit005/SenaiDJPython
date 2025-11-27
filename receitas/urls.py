from django.urls import path
from .views import home,sobre,receitas
urlpatterns = [
    path('',home),
    path('sobre/',sobre),
    path('receita/',receitas),
]
