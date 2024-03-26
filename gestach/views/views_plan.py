from django.shortcuts import render, redirect, get_object_or_404
from gestach.forms.forms_plan import ActionForm, ActionEquipeForm, ActiviteForm, TacheForm, ActiviteEquipeForm, \
    TacheEquipeForm, DiligenceForm
from gestach.models import Action, ActionEquipe, Activite, Tache, Diligence
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime, timedelta


def action_list(request):
    actions = Action.objects.all()

    # Valeurs de date par défaut (début et fin du mois en cours)
    today = datetime.today()
    start_of_month = today.replace(day=1)
    end_of_month = (start_of_month + timedelta(days=32)).replace(day=1) - timedelta(days=1)

    # Récupération des paramètres de recherche et de filtrage
    query = request.GET.get('q')
    start_date = request.GET.get('start_date', start_of_month.strftime('%Y-%m-%d'))
    end_date = request.GET.get('end_date', end_of_month.strftime('%Y-%m-%d'))

    # Filtrage des actions en fonction des paramètres
    if query:
        actions = actions.filter(
            Q(titre__icontains=query) |
            Q(description__icontains=query)
        )

    if start_date:
        start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
        actions = actions.filter(date_debut__gte=start_date)

    if end_date:
        end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
        actions = actions.filter(date_fin__lte=end_date)

    # Pagination
    paginator = Paginator(actions, 10)  # 10 actions par page
    page = request.GET.get('page')

    try:
        actions = paginator.page(page)
    except PageNotAnInteger:
        actions = paginator.page(1)
    except EmptyPage:
        actions = paginator.page(paginator.num_pages)

    return render(request, 'plan/action_list.html', {'actions': actions, 'start_date': start_date, 'end_date': end_date})


def action_detail(request, pk):
    action = get_object_or_404(Action, pk=pk)
    action_equipes = ActionEquipe.objects.filter(action=action)
    return render(request, 'plan/action_detail.html', {'action': action, 'action_equipes': action_equipes})


def agenda_perso(request, pk=None):
    return render(request,template_name='agenda_perso.html')


def action_create(request):
    if request.method == 'POST':
        form = ActionForm(request.POST)
        if form.is_valid():
            action = form.save()
            return redirect('plan:action_list')
    else:
        form = ActionForm()
    return render(request, 'plan/action_form.html', {'form': form})


def action_update(request, pk):
    action = get_object_or_404(Action, pk=pk)
    if request.method == 'POST':
        form = ActionForm(request.POST, instance=action)
        if form.is_valid():
            form.save()
            return redirect('plan:action_detail', pk=action.pk)
    else:
        form = ActionForm(instance=action)
    return render(request, 'plan/action_form.html', {'form': form})


def action_delete(request, pk):
    action = get_object_or_404(Action, pk=pk)
    if request.method == 'POST':
        action.delete()
        return redirect('plan:action_list')
    return render(request, 'plan/action_confirm_delete.html', {'action': action})


def action_equipe_create(request, action_pk):
    action = get_object_or_404(Action, pk=action_pk)
    if request.method == 'POST':
        form = ActionEquipeForm(request.POST)
        if form.is_valid():
            action_equipe = form.save(commit=False)
            action_equipe.action = action
            action_equipe.save()
            return redirect('plan:action_detail', pk=action.pk)
    else:
        form = ActionEquipeForm()
    return render(request, 'plan/action_equipe_form.html', {'form': form, 'action': action})


def action_equipe_update(request, pk):
    action_equipe = get_object_or_404(ActionEquipe, pk=pk)
    if request.method == 'POST':
        form = ActionEquipeForm(request.POST, instance=action_equipe)
        if form.is_valid():
            form.save()
            return redirect('plan:action_list', pk=action_equipe.pk)
    else:
        form = ActionForm(instance=action_equipe)
    return render(request, 'plan/action_equipe_form.html', {'form': form})


def activite_list(request):
    activites = Activite.objects.all()
    return render(request, 'plan/activite_list.html', {'activites': activites})


def activite(request):
    mon_activite = get_object_or_404(Activite)
    return render(request, 'plan/activite.html')


def activite_detail(request, pk):
    activite = get_object_or_404(Activite, pk=pk)
    return render(request, 'plan/activite_detail.html', {'activite': activite})


def activite_create(request):
    if request.method == 'POST':
        form = ActiviteForm(request.POST)
        if form.is_valid():
            activite = form.save()
            return redirect('plan:activite_detail', pk=activite.pk)
    else:
        form = ActiviteForm()
    return render(request, 'plan/activite_form.html', {'form': form})


def activite_update(request, pk):
    activite = get_object_or_404(Activite, pk=pk)
    if request.method == 'POST':
        form = ActiviteForm(request.POST, instance=activite)
        if form.is_valid():
            activite = form.save()
            return redirect('plan:activite_detail', pk=activite.pk)
    else:
        form = ActiviteForm(instance=activite)
    return render(request, 'plan/activite_form.html', {'form': form})


def activite_delete(request, pk):
    activite = get_object_or_404(Activite, pk=pk)
    if request.method == 'POST':
        activite.delete()
        return redirect('plan:activite_list')
    return render(request, 'plan/activite_confirm_delete.html', {'activite': activite})


def activite_equipe_create(request, activite_pk):
    activite = get_object_or_404(Activite, pk=activite_pk)
    if request.method == 'POST':
        form = ActiviteEquipeForm(request.POST)
        if form.is_valid():
            activite_equipe = form.save(commit=False)
            activite_equipe.action = activite.action  #
            activite_equipe.save()
            return redirect('plan:activite_detail', pk=activite.pk)
    else:
        form = ActiviteEquipeForm()
    return render(request, 'plan/activite_equipe_form.html', {'form': form, 'activite': activite})


# Vues pour Tache
def tache_list(request):
    taches = Tache.objects.all()
    return render(request, 'plan/tache_list.html', {'taches': taches})


def tache_detail(request, pk):
    tache = get_object_or_404(Tache, pk=pk)
    return render(request, 'plan/tache_detail.html', {'tache': tache})


def tache_create(request):
    if request.method == 'POST':
        form = TacheForm(request.POST)
        if form.is_valid():
            tache = form.save()
            return redirect('plan:tache_detail', pk=tache.pk)
    else:
        form = TacheForm()
    return render(request, 'plan/tache_form.html', {'form': form})


def tache_update(request, pk):
    tache = get_object_or_404(Tache, pk=pk)
    if request.method == 'POST':
        form = TacheForm(request.POST, instance=tache)
        if form.is_valid():
            tache = form.save()
            return redirect('plan:tache_detail', pk=tache.pk)
    else:
        form = TacheForm(instance=tache)
    return render(request, 'plan/tache_form.html', {'form': form})


def tache_delete(request, pk):
    tache = get_object_or_404(Tache, pk=pk)
    if request.method == 'POST':
        tache.delete()
        return redirect('plan:tache_list')
    return render(request, 'plan/tache_confirm_delete.html', {'tache': tache})


def tache_equipe_create(request, tache_pk):
    tache = get_object_or_404(Tache, pk=tache_pk)
    if request.method == 'POST':
        form = TacheEquipeForm(request.POST)
        if form.is_valid():
            tache_equipe = form.save(commit=False)
            tache_equipe.tache = tache
            tache_equipe.save()
            return redirect('plan:tache_detail', pk=tache.pk)
    else:
        form = TacheEquipeForm()
    return render(request, 'plan/tache_equipe_form.html', {'form': form, 'tache': tache})


def diligence_list(request):
    diligences = Diligence.objects.all()
    return render(request, 'plan/diligence_list.html', {'activites': diligences})


def diligence_detail(request):
    diligence = get_object_or_404(Diligence)
    return render(request, 'plan/diligence_detail.html')


def diligence_create(request):
    return render(request, 'plan/diligence_form.html')


def diligence_update(request, pk):
    diligence = get_object_or_404(Diligence, pk=pk)
    if request.method == 'POST':
        form = DiligenceForm(request.POST, instance=diligence)
        if form.is_valid():
            diligence = form.save()
            return redirect('plan:diligence_detail', pk=diligence.pk)
    else:
        form = ActiviteForm(instance=diligence)
    return render(request, 'plan/diligence_form.html', {'form': form})


def atelier(request):
    return render(request, 'plan/atelier_liste.html')


def agenda_perso(request):
    return render(request, 'agenda_perso.html')


def calendrier(request):
    return render(request, 'calendrier.html')