from django import forms
from .models import EmailSubscription
from captcha import fields, widgets
from django.utils.translation import gettext_lazy as _


class EmailSubscriptionForm(forms.ModelForm):
    """
    Email Subscription form.
    """
    email = forms.EmailField(label=_(''), widget=forms.EmailInput(attrs={'class':'me-1 px-2', 'placeholder':"Enter your email", "style": "height: 40px; border: none; width: 90%;"}))
    recaptcha = fields.ReCaptchaField(label='', widget=widgets.ReCaptchaV2Invisible)    
    class Meta:
        model = EmailSubscription
        fields = ('email',)
        


class ContactForm(forms.Form):
    last_name = forms.CharField(label=_('Last Name'), widget=forms.TextInput(attrs={'class':'form-control' })) 
    other_names = forms.CharField(label=_('Other Names'), widget=forms.TextInput(attrs={'class':'form-control' }))   
    email = forms.EmailField(label=_('Email'), widget=forms.EmailInput(attrs={'class':'form-control'}))
    message = forms.CharField(label=_('Message'), widget=forms.Textarea(attrs={'class':'form-control', 'rows':"12", 'placeholder':"Type the message you wish to send"}))
    recaptcha = fields.ReCaptchaField(label='', widget=widgets.ReCaptchaV2Invisible)