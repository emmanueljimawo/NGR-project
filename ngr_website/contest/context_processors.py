from .models import Contest
from django.conf import settings


def contest_processor(request):
    contest = Contest.objects.filter(active=True).first()
    currency = 'NGN'
    paystack_public_key= settings.PAYSTACK_PUBLIC_KEY

    return {'contest': contest, 'currency':currency, 'paystack_public_key':paystack_public_key}