"""
URL configuration for Django_Travelsite project.

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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path ,include
from Django_Travelsite import settings
from . import views
app_name = 'home_page'
urlpatterns = [
    path("",views.home_main_page,name="home_main_page"),
    path("about/",views.about_page,name="about_page"),
    path("elements/",views.elements,name="elements"),
    path('contact/',views.contact,name="contact"),
    path('newsletter/',views.newsletter,name="newsletter"),

]
