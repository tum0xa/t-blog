from django.contrib import admin
from django.urls import path
from . import views

app_name = 'mainapp'

urlpatterns = [
    path('', views.main, name="main"),
    path('subscribe/', views.subscribe, name="subscribe"),
    path('admin/', admin.site.urls),

]
