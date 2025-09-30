from captcha.fields import CaptchaField
from django import forms
from ..home_page.models import Contact

# class ContactModelForm(forms.ModelForm):
#     model = Contact
#     # captcha = CaptchaField()
#     exclude = ('created_date',)
