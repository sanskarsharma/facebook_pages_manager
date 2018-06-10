from django.urls import path
from . import views

app_name = "fbapp"
urlpatterns = [
    path('', views.home, name = "home"),
    path('dashboard', views.dashboard, name = "dashboard")
]