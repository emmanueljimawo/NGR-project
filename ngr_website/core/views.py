from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from .forms import ContactForm
from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.utils.safestring import mark_safe
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.

class Home(TemplateView):
    template_name = 'core/home.html'

class AboutUs(TemplateView):
    template_name = 'core/about-us.html'

class ContactUs(FormView):
    form_class = ContactForm
    template_name = 'core/contact-us.html'
    success_url = reverse_lazy('core:contact_us')

    def form_valid(self, form):
        """If the form is valid, redirect to the supplied URL."""
        subject = f'NGR Contact Form'
        from_email = settings.FROM_EMAIL
        last_name = form.cleaned_data['last_name']
        other_names = form.cleaned_data['other_names']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']
        try:
            send_mail(
                subject,
                f'Email: {email}\nLast Name: {last_name}\nOther Names: {other_names}\n\nMessage: {message}',
                from_email,
                [from_email],
                fail_silently=False,
            )
            messages.success(self.request, mark_safe(f'Your message has been sent!'))
        except:
            self.render_to_response(self.get_context_data(form=form))
            messages.error(self.request, mark_safe(f'Error! Message not sent!'))
        return super().form_valid(form)


    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        messages.error(self.request, mark_safe(f'Error! Message not sent!'))
        return self.render_to_response(self.get_context_data(form=form))

def subscribe(request):
    return render(request)


def custom_page_not_found_view(request, exception):
    return render(request, "errors/404.html", {})

def custom_error_view(request, exception=None):
    return render(request, "errors/500.html", {})

def custom_permission_denied_view(request, exception=None):
    return render(request, "errors/403.html", {})

def custom_bad_request_view(request, exception=None):
    return render(request, "errors/400.html", {})   





