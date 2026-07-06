from django.urls import path
from . import views

app_name = "home_page"
urlpatterns = [
    path("", views.home_main_page, name="home_main_page"),
    path("about/", views.about_page, name="about_page"),
    path("elements/", views.elements, name="elements"),
    path("contact/", views.contact, name="contact"),
    path("newsletter/", views.newsletter, name="newsletter"),
]
