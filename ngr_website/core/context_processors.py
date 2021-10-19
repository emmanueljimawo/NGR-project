from .forms import EmailSubscriptionForm
from .models import EmailSubscription

from django.shortcuts import redirect, render
from django.utils.safestring import mark_safe
from django.contrib import messages
from django.views.generic import FormView

def email_subscription_processor(request):
    return (request)
    
    # form_class = EmailSubscriptionForm
    # model = EmailSubscription

    # def form_valid(self, form):
    #     messages.success(self.request, mark_safe('Email submitted successfully'))
    #     return redirect('/')

    # def form_invalid(self, form):
    #     """If the form is valid, redirect to the supplied URL."""
    #     messages.error(self.request, mark_safe('Error submitting email'))
    #     return self.render_to_response(self.get_context_data(form=form))