from .import views
from django.urls import path

urlpatterns = [
    path('', views.home,name='home'),
    path('insert_builder',views.insert_builder,name='builder'),
    path('insert_applicant',views.insert_applicant,name='applicant'),
    path('login',views.login,name='commonlogin'),
]