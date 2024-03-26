from django.urls import path

from gestach.views.views_courrier import courrier_sortant, courrier_arrive, courrier_views

app_name = 'courrier'

urlpatterns = [
    path('courrier_sortant/', courrier_sortant, name='courrier_sortant'),
    path('courrier_arrive/', courrier_arrive, name='courrier_arrive'),
    path('courrier_views/', courrier_views, name='courrier_views'),

]
