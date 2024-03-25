from django.contrib.auth.models import User

from gestach.models import Utilisateur, Ministere, Direction
from django import forms
from django.contrib.auth import authenticate


class MinistereForm(forms.ModelForm):
    class Meta:
        model = Ministere
        fields = ['ministere', 'logo_min']


class DirectionForm(forms.ModelForm):
    class Meta:
        model = Direction
        fields = ['ministere', 'direction', 'logo_dir', 'bp_dir', 'adresse_dir']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['ministere'] = forms.ModelChoiceField(queryset=Ministere.objects.all())


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
            user = authenticate(username=email, password=password)

            if not user:
                # Le compte n'existe pas
                raise forms.ValidationError("L'email ou le mot de passe est incorrect")
            elif not user.is_active:
                # Le compte est désactivé
                raise forms.ValidationError("Ce compte est désactivé")

        return cleaned_data


class InscriptionForm(forms.Form):
    email = forms.EmailField(
        max_length=200,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Adresse email',
                'style': 'width: 100%'
            }
        )
    )

    def clean_email(self):
        email = self.cleaned_data['email']
        existing_user = Utilisateur.objects.filter(user__email=email).first()
        if existing_user:
            raise forms.ValidationError("Un compte avec cet email existe déjà.")
        return email


class InscriptionFinale(forms.Form):
    class Meta:
        model = Utilisateur
        fields = ['email', 'password', 'matricule', 'sexe']
        mon_matricule = 'GESTACH'  # Vous pouvez récupérer la civilité depuis le formulaire si nécessaire
        sexe = 'M'
        widgets = dict(email=forms.EmailInput(), password=forms.PasswordInput())


class FinalRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(label='Nouveau mot de passe', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Nouveau mot de passe', 'style': 'width: 100%'}))
    password2 = forms.CharField(label='Confirmer le mot de passe', widget=forms.PasswordInput(attrs={'class': 'form'
                                                                                                              '-control', 'placeholder': 'Confirmer le mot de passe', 'style': 'width: 100%'}))

    class Meta:
        model = User
        fields = ['email', 'last_name', 'first_name']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Adresse email', 'style': 'width: 100%'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom', 'style': 'width: 100%'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prénom', 'style': 'width: 100%'}),
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Les mots de passe ne correspondent pas.")

        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.is_active = True  # Activer le compte de l'utilisateur

        if commit:
            user.save()

        return user
