from django.shortcuts import render


def courrier_sortant(request):
    return render(request, 'courrier/courrier_sortant.html')


def courrier_arrive(request):
    return render(request, 'courrier/courrier_arrive.html')


def courrier_views(request):
    return render(request, 'courrier/courrier_views.html')
