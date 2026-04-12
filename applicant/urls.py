from .import views
from django.urls import path

urlpatterns = [
    path('', views.home,name='home'),
    path('req_home', views.req_home, name='request'),
    path('insert_complaint', views.insert_complaint, name='com'),
    path('show_reply', views.show_reply, name='reply'),


]