from django.views.generic import TemplateView


# Create your views here.

class Home(TemplateView):
    template_name = 'core/home.html'

class AboutUs(TemplateView):
    template_name = 'core/about-us.html'

class ContactUs(TemplateView):
    template_name = 'core/contact-us.html'


    
