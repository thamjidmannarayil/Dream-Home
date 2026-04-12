from .import views
from django.urls import path

urlpatterns = [
    path('', views.home,name='home'),
    path('show_notif', views.show_notif, name='notific'),
    path('insert_reqapply/<nid>', views.insert_reqapply, name='insert_reqapply'),
    path('update_req/<did>', views.update_req, name='up_req'),

]