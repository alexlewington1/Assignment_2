from django.shortcuts import render

def LandingPage(response):
    return render(response,"LandingPage.html")
def ProductPage(response):
    return render(response,"ProductPage.html")
def AboutUs(response):
    return render(response,"AboutUs.html")
def ContactUs(response):
    return render(response,"ContactUs.html")
