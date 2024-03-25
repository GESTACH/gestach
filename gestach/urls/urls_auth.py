from django.urls import path
from ..views.views_auth import tableaubord, user_register, user_pass_oublie, user_pass_reinit, admin_direction, \
    admin_ministere, user_register_success, user_final_inscription

app_name = 'auth'

urlpatterns = [
    path('dashbord/', tableaubord, name='tableau_bord'),
    path('user_final_inscription/<int:pk>/', user_final_inscription, name='user_final_inscription'),
    path('inscription/', user_register, name='user_register'),
    path('user_pass_oublie/', user_pass_oublie, name='user_pass_oublie'),
    path('user_register_success/<int:pk>/', user_register_success, name='user_register_success'),
    path('user_pass_reinit/', user_pass_reinit, name='user_pass_reinit'),
    path('admin_ministere/', admin_ministere, name='admin_ministere'),
    path('admin_direction/', admin_direction, name='admin_direction'),
]
