import secrets
import string

from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.template.loader import render_to_string
from django.urls import reverse

from DevaldoProject import settings
from gestach.forms.forms_auth import MinistereForm, DirectionForm, InscriptionForm, FinalRegistrationForm, ConnexionForm
from gestach.models import Ministere, Direction, Utilisateur


def admin_ministere(request):
    form = MinistereForm()  # Instanciez le formulaire en dehors du bloc if

    if request.method == 'POST':
        form = MinistereForm(request.POST)
        if form.is_valid():
            dep_ministere = Ministere()
            dep_ministere.ministere = form.cleaned_data['ministere'].upper()
            dep_ministere.logo_min = form.cleaned_data['logo_min']
            dep_ministere.save()
            # Traitement du formulaire
            return redirect('auth:admin_direction', ministere_id=dep_ministere.id)

    return render(request, 'auth/admin_ministere.html', {'form': form})


def admin_direction(request, ministere_id=None):
    initial_data = {'ministere': ministere_id}
    form = DirectionForm(initial=initial_data)

    if request.method == 'POST':
        form = DirectionForm(request.POST)

        if form.is_valid():
            min_direction = Direction()
            min_direction.ministere = form.cleaned_data['ministere']
            min_direction.direction = form.cleaned_data['direction'].upper()
            min_direction.adresse_dir = form.cleaned_data['adresse_dir']
            min_direction.bp_dir = form.cleaned_data['bp_dir']
            min_direction.logo_dir = form.cleaned_data['logo_dir']
            min_direction.save()

            # Redirection vers une URL appropriée après le traitement du formulaire
            return redirect('user_register')  # Assurez-vous que 'utilisateur_inscription' est correct

    return render(request, 'auth/admin_direction.html', {'form': form})


def tableaubord(request):
    return render(request, 'tableau_bord.html')


def index(request):
    if not Utilisateur.objects.exists():
        return redirect('auth:user_register')

    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                utilisateur = Utilisateur.objects.filter(user=user).first()
                if utilisateur:
                    return redirect('auth:tableau_bord', pk=utilisateur.pk)
                else:
                    messages.error(request, "Aucun compte utilisateur n'est associé à cet utilisateur.")
            else:
                messages.error(request, 'Email ou mot de passe incorrect.')
    else:
        form = ConnexionForm()

    return render(request, 'tableau_bord.html', {'form': form})


def generate_username():
    characters = string.ascii_lowercase + string.digits
    username = ''.join(secrets.choice(characters) for _ in range(12))
    return username


def generate_password():
    characters = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(characters) for _ in range(12))
    return password


def user_register(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            mon_username = generate_username()
            mon_password = generate_password()
            mon_matricule = 'GESTACH'  # Vous pouvez récupérer la civilité depuis le formulaire si nécessaire
            sexe = 'M'  # Vous pouvez récupérer le sexe depuis le formulaire si nécessaire

            try:
                # Création de l'utilisateur
                user = User.objects.create_user(username=mon_username, email=email, password=mon_password)

                # Création de l'objet Utilisateur associé
                mon_utilisateur = Utilisateur.objects.create(user=user, matricule=mon_matricule, sexe=sexe)

                # Envoi de l'email de confirmation
                html_content = render_to_string('auth/user_mail_register.html', {
                    'user': user,
                    'password': mon_password,
                })

                final_inscription_url = reverse('auth:user_final_inscription', args=[user.pk])
                html_content_with_url = html_content.replace('</body>',
                                                             f'<p><a href="{final_inscription_url}">Je finalier mon '
                                                             f'inscription par confirmation de mot de passe </a>et '
                                                             f'active automatiquement mon compte.</p></body>')

                subject = 'Confirmation de votre inscription'
                email = EmailMultiAlternatives(
                    subject=subject,
                    body='',  # Pas besoin de spécifier le corps, car vous utilisez le contenu HTML
                    from_email=settings.EMAIL_HOST_USER,
                    to=[email],
                )
                email.attach_alternative(html_content_with_url, "text/html")
                email.send(fail_silently=False)

                # Affichage d'un message de succès et redirection vers une page de succès
                messages.success(request, f"Votre compte a été créé avec succès. Veuillez consulter votre boîte de "
                                          f"réception à l'adresse  {email.to[0]} pour finaliser votre inscription.")
                return redirect(reverse('auth:user_register_success', args=[mon_utilisateur.pk]))

            except Exception as e:
                messages.error(request, f'Une erreur s\'est produite lors de la création de votre compte : {e}')
                return redirect('auth:user_register')
    else:
        form = InscriptionForm()
    return render(request, 'auth/user_register.html', {'form': form})


def user_register_success(request, pk):
    pk = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        messages.success(request, "Votre mot de passe a été modifié avec succès.")
        return redirect('index', pk=pk)
    return render(request, 'auth/user_register_success.html')


def user_pass_oublie(request):
    return render(request, 'auth/user_pass_oublie.html')


def user_pass_reinit(request):
    return render(request, 'auth/user_pass_reinit.html')


@login_required
def user_final_inscription(request, pk):
    user = get_object_or_404(User, pk=pk)

    if request.method == 'POST':
        form = FinalRegistrationForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save()
            # Authentifier l'utilisateur
            login(request, user)
            # Rediriger vers une page de succès ou effectuer d'autres actions
            return redirect('index')
    else:
        form = FinalRegistrationForm(instance=user)

    return render(request, 'auth/user_final_inscription.html', {'form': form})
