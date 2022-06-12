from django.urls import path
from . import views

#register app namespace
#URL NAMES
app_name = 'sample_app'

urlpatterns = [
    path('', views.home_view, name="home"),
    path('variables/', views.variables_view, name="variables")
]