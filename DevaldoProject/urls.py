"""
URL configuration for DevaldoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views. Home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from gestach.views import views_auth
from gestach.views import views_courrier
from gestach.views import views_rapport

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views_auth.index, name='index'),
    path('gestach/', include('gestach.urls.urls_auth')),
    path('gestach/', include('gestach.urls.urls_plan')),
    path('gestach/', include('gestach.urls.urls_courrier')),
    path('gestach/', include('gestach.urls.urls_rapport')),
]

