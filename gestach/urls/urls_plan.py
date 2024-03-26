from django.urls import path
from gestach.views.views_plan import (
    action_list,
    action_detail,
    action_create,
    action_update,
    action_delete,
    action_equipe_create,
    activite_list,
    activite_detail,
    activite_create,
    activite_update,
    activite_delete,
    activite_equipe_create,
    tache_list,
    tache_detail,
    tache_create,
    tache_update,
    tache_delete,
    tache_equipe_create, agenda_perso, activite, atelier, diligence_list, calendrier
)

app_name = 'plan'

urlpatterns = [
    path('actions_list/', action_list, name='action_list'),
    path('actions_detail/<int:pk>/', action_detail, name='action_detail'),
    path('actions_create/', action_create, name='action_create'),
    path('actions_update/<int:pk>/', action_update, name='action_update'),
    path('actions_delete/<int:pk>/', action_delete, name='action_delete'),
    path('actions_equipe_create/<int:action_pk>/', action_equipe_create, name='action_equipe_create'),
    path('actions_equipe_update/<int:pk>/', action_equipe_create, name='action_equipe_create'),

    path('activites_list/', activite_list, name='activite_list'),
    path('activites/', activite, name='activite'),
    path('activites_detail/<int:pk>/', activite_detail, name='activite_detail'),
    path('activites_create/', activite_create, name='activite_create'),
    path('activites_update/<int:pk>/', activite_update, name='activite_update'),
    path('activites_delete/<int:pk>/', activite_delete, name='activite_delete'),
    path('activites_equipe_create/<int:activite_pk>/', activite_equipe_create, name='activite_equipe_create'),

    path('taches_list/', tache_list, name='tache_list'),
    path('taches_detail/<int:pk>/', tache_detail, name='tache_detail'),
    path('taches_create/', tache_create, name='tache_create'),
    path('taches_update/<int:pk>/', tache_update, name='tache_update'),
    path('taches_delete/<int:pk>/', tache_delete, name='tache_delete'),
    path('taches_equipe_create/<int:tache_pk>/', tache_equipe_create, name='tache_equipe_create'),

    path('agenda_perso/', agenda_perso, name='agenda_perso'),
    path('atelier_list/', atelier, name='atelier_list'),
    path('diligence_list/', diligence_list, name='diligence_list'),
    path('calendrier/', calendrier, name='calendrier'),
]