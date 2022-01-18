from .forms import EmailSubscriptionForm
import settings


def processors(request):
    return {
        'subscription_form':EmailSubscriptionForm(),
        'facebook':settings.FACEBOOK,
        'twitter':settings.TWITTER,
        'instagram':settings.INSTAGRAM,
        'phone_number':settings.PHONE_NUMBER
        }
    
