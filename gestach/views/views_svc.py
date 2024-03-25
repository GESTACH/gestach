from django.shortcuts import render
from gestach.models import Ministere, Direction, Service, Employer


def ministere(request):
    return render(request, 'service/ministere.html')


def direction(request):
    return render(request, 'service/direction.html')


def ministere_liste(request):
    return render(request, 'service/ministere_liste.html')


def direction_liste(request):
    return render(request, 'service/direction_liste.html')


def service_liste(request):
    ministere_list = Ministere.objects.all()

    # Créer une liste de dictionnaires pour stocker les données à afficher
    data = []

    for ministere in ministere_list:
        ministere_data = {
            'ministere': ministere,
            'directions': []
        }

        directions = Direction.objects.filter(ministere=ministere)

        for direction in directions:
            direction_data = {
                'direction': direction,
                'services': list(Service.objects.filter(direction=direction).values('name', 'id'))
            }

            for service in direction_data['services']:
                service['employers'] = list(Employer.objects.filter(service_id=service['id']).values('user__user__username', 'fonction'))

            ministere_data['directions'].append(direction_data)

        data.append(ministere_data)

    return render(request, 'service/service_liste.html', {'data': data})
