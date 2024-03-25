# core/admin.py

from django.contrib import admin
from gestach.models import Utilisateur, EmailConfirmation,  Ministere, Direction, Service, TypeAction, \
    Activite, ActionEquipe, Action, ActiviteEquipe, Tache, TacheEquipe, TypeNotification, Notification, \
    DestinataireNotification, Document, Rapport, AppreciationRapport, StatutCourrier, Courrier, \
    Diligence, DiligenceEquipe


admin.site.register(Utilisateur)
admin.site.register(EmailConfirmation)
admin.site.register(Ministere)
admin.site.register(Direction)
admin.site.register(Service)
admin.site.register(TypeAction)
admin.site.register(Action)
admin.site.register(ActionEquipe)
admin.site.register(Activite)
admin.site.register(ActiviteEquipe)
admin.site.register(Tache)
admin.site.register(TacheEquipe)
admin.site.register(Diligence)
admin.site.register(DiligenceEquipe)
admin.site.register(TypeNotification)
admin.site.register(Notification)
admin.site.register(DestinataireNotification)
admin.site.register(Document)
admin.site.register(Rapport)
admin.site.register(AppreciationRapport)
admin.site.register(StatutCourrier)
admin.site.register(Courrier)

