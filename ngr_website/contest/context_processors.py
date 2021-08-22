import uuid
from .models import Contest
from django.conf import settings


def contest_processor(request):
    contest = Contest.objects.filter(active=True).first()
    currency = 'NGN'
    ref_number = f'{uuid.uuid4().hex}'
    paystack_public_key= settings.PAYSTACK_PUBLIC_KEY

    return {'contest': contest, 'currency':currency, 'paystack_public_key':paystack_public_key, 'ref_number':ref_number}

