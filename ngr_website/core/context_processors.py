from .forms import EmailSubscriptionForm
from django.conf import settings


def processors(request):
    return {
        'subscription_form':EmailSubscriptionForm(),
        'facebook':settings.FACEBOOK,
        'twitter':settings.TWITTER,
        'instagram':settings.INSTAGRAM,
        'phone_number':settings.PHONE_NUMBER
        }
    
