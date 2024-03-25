# models.py

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Utilisateur(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo_utilisateur = models.ImageField(upload_to='utilisateurs/', null=True, blank=True)
    sexe = models.CharField(max_length=2, choices=(('M', 'M'), ('F', 'F')), default='M.')
    adresse = models.CharField(max_length=255, null=True)
    date_naissance = models.DateField(null=True, blank=True)
    lieu_naissance = models.CharField(max_length=255)
    Nom_pere = models.CharField(max_length=255)
    nom_mere = models.CharField(max_length=255)
    matricule = models.CharField(max_length=20, null=True)
    num_cni = models.CharField(max_length=15)
    date_cni = models.DateField(null=True, blank=True)
    hors_service = models.BooleanField(default=False)
    vehicule = models.BooleanField(default=False)
    vehicule_immatriculation = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.user.last_name


class EmailConfirmation(models.Model):
    email_confirmation = models.EmailField(max_length=255)
    email_date = models.DateTimeField(default=timezone.now)


class Ministere(models.Model):
    ministere = models.CharField(max_length=255)
    logo_min = models.ImageField(upload_to='logo/', null=True, blank=True)

    def __str__(self):
        return self.ministere


class Direction(models.Model):
    ministere = models.ForeignKey(Ministere, on_delete=models.CASCADE, related_name='directions')
    direction = models.CharField(max_length=255)
    logo_dir = models.ImageField(upload_to='logo/', null=True, blank=True)
    bp_dir = models.CharField(max_length=255)
    adresse_dir = models.CharField(max_length=255)

    def __str__(self):
        return self.direction


class Service(models.Model):
    name = models.CharField(max_length=255)
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE, related_name='services')

    def __str__(self):
        return self.name


class Employer(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='appartenances_user')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='services')
    fonction = models.TextField()


class Diligence(models.Model):
    titre = models.CharField(max_length=255)
    description = models.TextField()
    date_debut = models.DateField()
    date_fin = models.DateField()
    duree = models.IntegerField()
    statut = models.CharField(max_length=30)

    def __str__(self):
        return self.titre


class DiligenceEquipe(models.Model):
    diligence = models.ForeignKey(Diligence, on_delete=models.CASCADE, related_name='diligences')
    employee = models.ForeignKey(Employer, on_delete=models.CASCADE, related_name='employers')
    chef_equipe = models.BooleanField(default=False)


class TypeAction(models.Model):
    nom = models.CharField(max_length=255)

    def __str__(self):
        return self.nom


class Action(models.Model):
    titre = models.CharField(max_length=255)
    type_action = models.ForeignKey(TypeAction, on_delete=models.CASCADE, related_name='actions')
    description = models.TextField()
    date_debut = models.DateField()
    date_fin = models.DateField()
    duree = models.IntegerField()
    statut = models.CharField(max_length=30)

    def __str__(self):
        return self.titre


class ActionEquipe(models.Model):
    action = models.ForeignKey(Action, on_delete=models.CASCADE, related_name='action_equipes')
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE, related_name='action_employers')
    chef_equipe = models.BooleanField(default=False)
    date_action = models.DateField(default=timezone.now)


class Activite(models.Model):
    action_parente = models.ForeignKey(Action, on_delete=models.CASCADE, related_name='activites')
    titre = models.CharField(max_length=255)
    type_activite = models.ForeignKey(TypeAction, on_delete=models.CASCADE)
    description = models.TextField()
    date_debut = models.DateField()
    date_fin = models.DateField()
    duree = models.IntegerField()
    statut = models.CharField(max_length=30)

    def __str__(self):
        return self.titre


class ActiviteEquipe(models.Model):
    action = models.ForeignKey(Action, on_delete=models.CASCADE, related_name='activite_equipe')
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE, related_name='activite_employers')
    chef_equipe = models.BooleanField(default=False)
    date_action = models.DateField(default=timezone.now)


class Tache(models.Model):
    activite_parente = models.ForeignKey(Activite, on_delete=models.CASCADE, related_name='taches')
    titre = models.CharField(max_length=255)
    type_tache = models.ForeignKey(TypeAction, on_delete=models.CASCADE)
    description = models.TextField()
    date_debut = models.DateField()
    date_fin = models.DateField()
    duree = models.IntegerField()
    statut = models.CharField(max_length=30)

    def __str__(self):
        return self.titre


class TacheEquipe(models.Model):
    tache = models.ForeignKey(Tache, on_delete=models.CASCADE, related_name='tache_equipe')
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE, related_name='tache_employer')
    chef_equipe = models.BooleanField(default=False)
# Permissions
# Notifications


class Atelier(models.Model):
    titre = models.CharField(max_length=255)
    description = models.TextField()
    date_debut = models.DateField()
    date_fin = models.DateField()
    duree = models.IntegerField()
    statut = models.CharField(max_length=30)

    def __str__(self):
        return self.titre


class AtelierEquipe(models.Model):
    action = models.ForeignKey(Action, on_delete=models.CASCADE, related_name='atelier_equipes')
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE, related_name='atelier_employers')
    chef_equipe = models.BooleanField(default=False)
    date_action = models.DateField(default=timezone.now)


class TypeNotification(models.Model):
    nom = models.CharField(max_length=255)

    def __str__(self):
        return self.nom


class Notification(models.Model):
    type = models.ForeignKey(TypeNotification, on_delete=models.CASCADE, related_name='notifications')
    contenu = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    utilisateurs = models.ManyToManyField(Utilisateur, through='DestinataireNotification', related_name='notifications')


class DestinataireNotification(models.Model):
    notification = models.ForeignKey(Notification, on_delete=models.CASCADE, related_name='notifications')
    utilisateurs = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='notifications_employer')


# Documents et rapports
class Document(models.Model):
    titre = models.CharField(max_length=255)
    fichier = models.FileField()
    auteur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name="documents")
    date = models.DateField(auto_now_add=True)


class Rapport(Document):
    destinateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name="rapports")


class AppreciationRapport(models.Model):
    rapport = models.ForeignKey(Rapport, on_delete=models.CASCADE)
    emetteur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name="appreciations")
    commentaires = models.TextField()


# Courriers
class StatutCourrier(models.Model):
    nom = models.CharField(max_length=255)


class Courrier(Document):
    expediteur = models.CharField(max_length=120, null=True, blank=True)
    statut = models.ForeignKey(StatutCourrier, on_delete=models.CASCADE, null=True, blank=True)
    destinataires = models.ManyToManyField(Utilisateur, related_name='courriers_recus')
    observations = models.TextField(blank=True)
    valide = models.BooleanField(default=False)

    def soumettre_validation(self):
        self.observations = None
        self.valide = False
        self.save()
        # Envoyer une notification au supérieur

    def valider(self):
        self.valide = True
        self.save()
        # Notification de validation

    def retour_correction(self, observations):
        self.observations = observations
        self.save()
        # Notification de retour pour correction