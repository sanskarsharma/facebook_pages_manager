from django.urls import path
from . import views

app_name = "fbapp"
urlpatterns = [
    path('', views.home, name = "home"),
    path('dashboard', views.dashboard, name = "dashboard"),
    path('page_detail', views.get_page_details, name= "page_detail"),
    path('update_form', views.get_form, name="update_form")
]







