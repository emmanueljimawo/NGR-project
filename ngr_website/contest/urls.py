from django.urls import path
from .views import Contestants, Profile, Registration, verify_registration_fee_payment

app_name = 'contest'

urlpatterns = [
    path('registration/', Registration.as_view(), name='registration'),
    path('contestants/profile/<slug:slug>/', Profile.as_view(), name='profile'),
    # path('contestants/payment/<str:slug>/', Payment.as_view(), name='payment'),
    # path('contestants/profile', Profile.as_view(), name='profile'),
    path('contestants/', Contestants.as_view(), name='contestants'),
    path('<str:ref>/', verify_registration_fee_payment, name='verify_registration_fee_payment'),

]
