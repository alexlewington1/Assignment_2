from django.urls import path
from . import views
urlpatterns = [
    path("", views.LandingPage, name="LandingPage"),
    path("about/", views.AboutUs, name="AboutUs"),
    path("contactus/", views.ContactUs, name="ContactUs"),
    path("products/", views.ProductPage, name="ProductPage"),

]