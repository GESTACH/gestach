from django.urls import path

from gestach.views.views_rapport import rapport_views, rapport_list, rapport_creat

app_name = 'rapport'

urlpatterns = [
    path('rapport_list/', rapport_list, name='rapport_list'),
    path('rapport_creat/', rapport_creat, name='rapport_creat'),
    path('rapport_view/', rapport_views, name='rapport_view'),

]
