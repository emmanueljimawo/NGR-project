from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import Contestants, Profile, Registration, verify_registration_fee_payment, verify_voting_fee_payment

app_name = 'contest'

handler404 = 'core.views.custom_page_not_found_view'
handler500 = 'core.views.custom_error_view'
handler403 = 'core.views.custom_permission_denied_view'
handler400 = 'core.views.custom_bad_request_view'


urlpatterns = [
    path('registration/', Registration.as_view(), name='registration'),
    path('contestants/<slug:slug>/', Profile.as_view(), name='profile'),
    path('contestants/', Contestants.as_view(), name='contestants'),
    path('registration/<str:ref>/', verify_registration_fee_payment, name='verify_registration_fee_payment'),
    path('voting/<slug:slug>/<str:ref>/', verify_voting_fee_payment, name='verify_voting_fee_payment'),
]
