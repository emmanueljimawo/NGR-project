import json
from django.core.mail import send_mail
from django.http.response import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404
from django.urls.base import reverse
from django.utils.safestring import mark_safe
from django.views.generic import FormView, ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView
from .forms import PaymentForm, RegistrationForm
from .models import Contest, Contestant, Vote
import uuid
from django.utils.text import slugify
from django.contrib import messages
from django.db.models import Q, Sum

import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from paystackapi.paystack import Paystack
from django.conf import settings
paystack = Paystack(secret_key=settings.PAYSTACK_SECRET_KEY)


@csrf_exempt
@require_POST
def webhook_endpoint(request):
    jsondata = request.body
    data = json.loads(jsondata)
    if data['data']['status'] == 'success':
        slug = data['data']['metadata']['custom_fields'][0]['slug']
        payment_type = data['data']['metadata']['custom_fields'][0]['payment_type'] # vote or register
        ref = data['data']['reference']
        amount_paid = data['data']['amount'] / 100
        contestant = get_object_or_404(Contestant, slug=slug)
        if payment_type == 'vote':
            votes_count = amount_paid/contestant.contest.voting_fee_amount
            Vote.objects.create(ref_number=ref, contestant=contestant, amount_paid=amount_paid, payment_verified = True, votes_count=votes_count)
        elif payment_type == 'register':
            contestant.ref_number = ref
            contestant.payment_verified = True
            contestant.save()
    return HttpResponse(status=200)




# Create your views here.

class Registration(FormView):
    form_class = RegistrationForm
    model = Contestant
    template_name = 'contest/registration.html'

    def form_valid(self, form):
        """If the form is valid, redirect to the supplied URL."""
        contest = Contest.objects.filter(active=True).first()
        # ref_number = slugify(f"{form.cleaned_data['last_name'].lower()} {contest.title.lower()} {uuid.uuid4().hex}")
        self.object = form.save(commit=False)
        self.object.contest = contest 
        self.object.agree_to_the_terms_and_conditions = True 
        self.object.agree_to_pay_the_registration_fee = True 
        self.object.agree_that_the_information_provided_is_accurate = True 
        self.object.save()
        self.object.refresh_from_db()
        subject = f'NGR Registration'
        from_email = 'NGR <gigantlimited@gmail.com>'
        to_email = form.cleaned_data['email']
        name = f"{form.cleaned_data['last_name']} {form.cleaned_data['other_names']}"

        try:
            send_mail(
                subject,
                f'Dear {name}\n\nThank you for your interest in registering for the "{contest}" contest. Kindly complete your registration by going to the following link.\nhttps://naijagracerace.com/contest/contestants/{self.object.slug}',
                from_email,
                [to_email],
                fail_silently=False,
            )
        except Exception as e:
            print(f'Error sending email. The error is {e}')
        return HttpResponseRedirect(reverse('contest:profile', kwargs={'slug': self.object.slug}))


class Profile(UpdateView):
    template_name = 'contest/profile.html'
    form_class = PaymentForm
    model = Contestant

    def get_success_url(self):
        messages.success(self.request, mark_safe('Profile updated successfully'))
        return reverse('contest:profile', kwargs={'slug': self.object.slug})

    def form_invalid(self, form):
        """If the form is valid, redirect to the supplied URL."""
        messages.error(self.request, mark_safe('Profile updated unsuccessful'))
        return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vote_count'] = Vote.objects.filter(contestant=self.object.id).aggregate(no = Sum('votes_count'))
        context['vote_payment_type'] = 'vote'
        context['register_payment_type'] = 'register'
        return context



class Contestants(ListView):
    model = Contestant
    template_name = 'contest/contestants.html'
    paginate_by = 40

    def get_queryset(self, **kwargs):
        try:
            keyword = self.request.GET['q']
        except:
            keyword = ''
        if (keyword != ''):
            object_list = sorted(self.model.objects.filter(
                Q(state__istartswith=keyword) | Q(last_name__istartswith=keyword) | Q(other_names__icontains=keyword) | Q(email__istartswith=keyword), payment_verified=True), key= lambda  t: t.count_votes(), reverse=True).annotate(vote_count = Sum('vote__votes_count'))
                
        else:
            object_list = sorted(self.model.objects.all().annotate(vote_count = Sum('vote__votes_count')), key= lambda  t: t.count_votes(), reverse=True)
 
        return object_list


# def verify_registration_fee_payment(request, ref):
#     contestant = get_object_or_404(Contestant, ref_number=ref)
#     payment_verified = contestant.verify_payment()
#     if payment_verified:
#         messages.success(request, mark_safe('Registration payment successful'))
#     else:
#         messages.error(request, mark_safe('Registration payment failed'))
#     return HttpResponseRedirect(reverse('contest:profile', kwargs={'slug': contestant.slug}))


# def verify_voting_fee_payment(request, slug, ref):
#     contestant = get_object_or_404(Contestant, slug=slug)
#     vote = Vote.objects.create(ref_number=ref, contestant=contestant)
#     print(f'This is ref: {ref}')
#     payment_verified = vote.verify_payment()
#     if payment_verified:
#         messages.success(request, mark_safe('Voted successfully'))
#     else:
#         messages.error(request, mark_safe('Voting failed'))
#     return HttpResponseRedirect(reverse('contest:profile', kwargs={'slug': contestant.slug}))


def verify_registration_fee_payment(request, slug, ref):
    contestant = get_object_or_404(Contestant, slug=slug)
    payment_verified = paystack.transaction.verify(ref)['status']
    if payment_verified:
        messages.success(request, mark_safe('Registration payment successful'))
    else:
        messages.error(request, mark_safe('Registration payment failed'))
    return HttpResponseRedirect(reverse('contest:profile', kwargs={'slug': contestant.slug}))

def verify_voting_fee_payment(request, slug, ref):
    contestant = get_object_or_404(Contestant, slug=slug)
    payment_verified = paystack.transaction.verify(ref)['status']
    if payment_verified:
        messages.success(request, mark_safe('Voted successfully'))
    else:
        messages.error(request, mark_safe('Voting failed'))
    return HttpResponseRedirect(reverse('contest:profile', kwargs={'slug': contestant.slug}))


def paystack_webhook(request):
    return JsonResponse(json.dumps(request.POST), safe=False)