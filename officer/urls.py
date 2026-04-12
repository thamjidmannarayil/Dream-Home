from .import views
from django.urls import path

urlpatterns = [
    path('', views.home,name='home'),
    path('update_office', views.update_office, name='up_off'),
    path('delete_office', views.delete_office, name='del_off'),
    path('insert_project', views.insert_project, name='proj'),
    path('update_project/<did>', views.update_project, name='up_proj'),
    path('delete_project/<did>', views.delete_project, name='del_proj'),
    path('insert_plot', views.insert_plot, name='plot'),
    path('update_plot/<did>', views.update_plot, name='up_plot'),
    path('delete_plot/<did>', views.delete_plot, name='dele_plot'),
    path('show_request', views.show_request, name='show_request'),
    path('verify/<did>', views.verify, name='verify'),
    path('insert_notif', views.insert_notif, name='notif'),
    path('apply_notif/<did>', views.apply_notif, name='up_notif'),
    path('show_complaint', views.show_complaint, name='show_complaint'),
    path('insert_reply/<cid>', views.insert_reply, name='insert_reply'),
    path('insert_survey', views.insert_survey, name='survey'),
    path('show_builder', views.show_builder, name='show_builder'),
    path('activate_builder/<sid>', views.activate_builder, name='activate_builder'),
    path('show_reapply/<id>', views.show_reapply, name='show_reqapply'),
    path('activate_builderQuote/<sid>', views.activate_builderQuote, name='activate_builderQuote'),
    path('notification_list', views.notification_list, name='notification_list'),
    path('approved_quotationlist/<id>', views.approved_quotationlist, name='approved_quotationlist'),
    path('notification_list_approved', views.notification_list_approved, name='notification_list_approved'),
    path('view_project1', views.view_project1, name='view_project1'),
    path('more_request1/<id>', views.more_request1, name='more_request1'),
    path('approve_projectlist', views.approve_projectlist, name='approve_projectlist'),

]