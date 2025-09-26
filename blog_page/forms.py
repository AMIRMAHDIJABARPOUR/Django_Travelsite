from django import forms
from .models import Contact

class ContactModelForm(forms.ModelForm):
    model = Contact
    exclude = ('created_date',)
