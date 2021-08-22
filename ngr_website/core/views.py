from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class Home(TemplateView):
    template_name = 'core/home.html'

class AboutUs(TemplateView):
    template_name = 'core/about-us.html'

class ContactUs(TemplateView):
    template_name = 'core/contact-us.html'


def custom_page_not_found_view(request, exception):
    return render(request, "errors/404.html", {})

def custom_error_view(request, exception=None):
    return render(request, "errors/500.html", {})

def custom_permission_denied_view(request, exception=None):
    return render(request, "errors/403.html", {})

def custom_bad_request_view(request, exception=None):
    return render(request, "errors/400.html", {})   
