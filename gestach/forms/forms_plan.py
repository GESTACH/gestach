from django import forms
from gestach.models import Action, Activite, ActionEquipe, Tache, ActiviteEquipe, TacheEquipe, Diligence


class ActionForm(forms.ModelForm):
    class Meta:
        model = Action
        fields = ['titre', 'type_action', 'description', 'date_debut', 'duree', 'date_fin']
        widgets = {
            'titre': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 100%'}),
            'type_action': forms.Select(attrs={'class': 'form-control', 'style': 'width: 100%'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'style': 'width: 100%'}),
            'date_debut': forms.DateInput(attrs={'class': 'form-control', 'style': 'width: 100%'}),
            'duree': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 100%'}),
        }

class ActionEquipeForm(forms.ModelForm):
    class Meta:
        model = ActionEquipe
        fields = ['employer', 'chef_equipe', 'date_action']


class ActiviteForm(forms.ModelForm):
    class Meta:
        model = Activite
        fields = ['titre', 'type_activite', 'description', 'date_debut', 'date_fin', 'duree']


class ActiviteEquipeForm(forms.ModelForm):
    class Meta:
        model = ActiviteEquipe
        fields = ['employer', 'chef_equipe', 'date_action']


class TacheForm(forms.ModelForm):
    class Meta:
        model = Tache
        fields = ['titre', 'type_tache', 'description', 'date_debut', 'date_fin', 'duree', 'statut']


class TacheEquipeForm(forms.ModelForm):
    class Meta:
        model = TacheEquipe
        fields = ['tache', 'employer', 'chef_equipe']


class DiligenceForm(forms.ModelForm):
    class Meta:
        model = Diligence
        fields = ['titre', 'description', 'date_debut', 'date_fin', 'duree']


