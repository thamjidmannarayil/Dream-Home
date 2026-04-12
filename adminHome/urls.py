from .import views
from django.urls import path

urlpatterns = [
    path('', views.home,name='home'),
    path('insert_designation',views.insert_designation,name='designation'),
    path('update_designation/<did>',views.update_designation,name='up_desi'),
    path('delete_designation/<did>',views.delete_designation,name='dele_desi'),
    path('insert_district',views.insert_district,name='dist'),
    path('update_district/<did>', views.update_district, name='up_dist'),
    path('delete_district/<did>', views.delete_district, name='dele_dist'),
    path('insert_vlg',views.insert_vlg,name='vlg'),
    path('update_vlg/<did>', views.update_vlg, name='up_vlg'),
    path('delete_vlg/<did>', views.delete_vlg, name='dele_vlg'),
    path('insert_qt', views.insert_qt, name='qt'),
    path('update_quote/<did>', views.update_quote, name='up_qt'),
    path('delete_quote/<did>', views.delete_quote, name='dele_qt'),
    path('add_office', views.add_office, name='office1'),
    path('insert_FAQ', views.insert_FAQ, name='faqQuest'),
    path('view_applicant', views.view_applicant, name='view_applicant'),
    path('view_project', views.view_project, name='view_project'),
    path('more_request/<id>', views.more_request, name='more_request'),





]
