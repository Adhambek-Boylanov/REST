"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from configapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',actor_get_post),
    path('actor/<int:pk>/',actor_put),
    path('movie/',MovieApi.as_view()),
    path("movie/<int:pk>/",MovieDetailAPI.as_view()),
    path('movies/<int:start_year>/', MovieDataAPI.as_view()),
    path('movies/<int:start_year>/<int:end_year>/', MovieDataAPI.as_view()),
    path('movies/', MovieDataAPI.as_view()),
]
