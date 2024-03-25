from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Utilisateur
from django import forms
from django.contrib.auth import authenticate
from gestach.models import Action, ActionEquipe


class ConnexionForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")
        if email and password:
            # Authentification utilisateur
            user = authenticate(email=email, password=password)

            if not user:
                # Le compte n'existe pas
                raise forms.ValidationError("L'email ou le mot de passe est incorrect")
            elif not user.is_active:
                # Le compte est désactivé
                raise forms.ValidationError("Ce compte est désactivé")

        return cleaned_data


class InscriptionForm(UserCreationForm):
    email = forms.EmailField(
        max_length=200,
        widget=forms.EmailInput(attrs={'class': 'form-control is-valid', 'placeholder': 'Email'})
    )

    class Meta:
        model = User
        fields = ['email']


class ConfirmationForm(forms.Form):
    # Ajoutez les champs nécessaires pour le formulaire de confirmation
    # Par exemple, un champ de texte, etc.
    message = forms.CharField(widget=forms.Textarea)


class InscriptionFinale(forms.Form):
    class Meta:
        model = Utilisateur
        fields = ['email', 'password']
        widgets = dict(email=forms.EmailInput(), password=forms.PasswordInput())


class ActionForm(forms.ModelForm):
    class Meta:
        model = Action
        fields = ['titre', 'type_action', 'description', 'date_debut', 'date_fin', 'duree', 'statut']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class ActionEquipeForm(forms.ModelForm):
    class Meta:
        model = ActionEquipe
        fields = ['action', 'employer', 'chef_equipe']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'