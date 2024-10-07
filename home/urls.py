from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('run_scrapper/', views.run_scrapper, name='run_scrapper'),
]