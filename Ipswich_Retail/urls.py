from django.urls import path
from . import views
urlpatterns = [
    path("", views.LandingPage, name="LandingPage"),
    path("about/", views.AboutPage, name="AboutPage"),
    path("contactus/", views.ContactUs, name="ContactUs"),
    path("products/", views.ProductPage, name="ProductPage"),

]