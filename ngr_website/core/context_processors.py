from .forms import EmailSubscriptionForm


def email_subscription_processor(request):
    return {'subscription_form':EmailSubscriptionForm()}
    
