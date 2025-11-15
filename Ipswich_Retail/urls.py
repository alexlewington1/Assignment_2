from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.LandingPage, name="LandingPage"),
    path("about/", views.AboutUs, name="AboutUs"),
    path("contactus/", views.ContactUs, name="ContactUs"),
    path("products/", views.products_view, name="ProductPage"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)