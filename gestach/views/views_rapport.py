from django.shortcuts import render


def rapport_list(request):
    return render(request, 'rapport/rapport_list.html')


def rapport_creat(request):
    return render(request, 'rapport/rapport_creat.html')


def rapport_views(request):
    return render(request, 'rapport/rapport_views.html')