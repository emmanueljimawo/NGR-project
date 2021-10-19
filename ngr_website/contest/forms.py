from django import forms
from .models import Contestant
from django.utils.translation import gettext_lazy as _
from captcha import fields, widgets



class RegistrationForm(forms.ModelForm):
    """
    Registration form for contestants.
    """
    recaptcha = fields.ReCaptchaField(label='', widget=widgets.ReCaptchaV2Invisible)
    phone_number = forms.CharField(help_text=_('Phone number should be 11 digits'), label=_("Phone number (080****)"), widget=forms.TextInput(attrs={'class': 'form-control', 'pattern':'^0\d{10}$'}))
    profession = forms.CharField(label=_("What do you do?"), widget=forms.TextInput(attrs={'class':'form-control', }))
    about = forms.CharField(label=_('About you'), widget=forms.Textarea(attrs={'class':'form-control' }))
    photograph = forms.ImageField(help_text=_('Recommended size: 1080 x 1920 pixels'), widget=forms.FileInput(attrs={'class': 'form-control', }))


    class Meta:
        model = Contestant
        exclude = ['date_created', 'date_modified',
                   'contest', 'ref_number', 'payment_verified', 'slug']
        widgets = {
          'last_name': forms.TextInput(attrs={'class': 'form-control', }),
          'other_names': forms.TextInput(attrs={'class':'form-control', }),
          'age': forms.NumberInput(attrs={'class':'form-control', }),
          'sex': forms.Select(attrs={'class': 'form-control', }),
          'facebook': forms.URLInput(attrs={'class':'form-control', }),
          'instagram': forms.URLInput(attrs={'class':'form-control', }),
          'twitter': forms.URLInput(attrs={'class':'form-control', }),
          'email': forms.EmailInput(attrs={'class':'form-control', }),
          'state': forms.Select(attrs={'class':'form-control', }),
        }


class PaymentForm(forms.ModelForm):
    """
    Payment form for contestants.
    """
    recaptcha = fields.ReCaptchaField(label='', widget=widgets.ReCaptchaV2Invisible)
    last_name = forms.CharField(disabled=True)
    other_names = forms.CharField(disabled=True)
    age = forms.CharField(disabled=True)
    sex = forms.CharField(disabled=True)
    email = forms.CharField(disabled=True)
    phone_number = forms.CharField(help_text=_('Phone number should be 11 digits'), label=_("Phone number (080****)"), widget=forms.TextInput(attrs={'class': 'form-control', 'pattern':'^0\d{10}$'}))
    profession = forms.CharField(label=_("What do you do?"), widget=forms.TextInput(attrs={'class':'form-control', }))
    about = forms.CharField(label=_('About you'), widget=forms.Textarea(attrs={'class':'form-control' }))


    class Meta:
        model = Contestant
        exclude = ['date_created', 'date_modified',
                   'contest', 'ref_number', 'payment_verified', 'slug']
        widgets = {
          'facebook': forms.URLInput(attrs={'class':'form-control', }),
          'instagram': forms.URLInput(attrs={'class':'form-control', }),
          'twitter': forms.URLInput(attrs={'class':'form-control', }),
          'state': forms.Select(attrs={'class':'form-control', }),
          'photograph': forms.FileInput(attrs={'class': 'form-control', }),
        }
