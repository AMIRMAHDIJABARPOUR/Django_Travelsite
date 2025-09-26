from django import forms
from .models import Contact , Newsletter

class ContactModelForm(forms.ModelForm):

    class Meta:
        model = Contact
        exclude = ('created_date',)
        fields = ['name','email','subject','massage']

class NewsletterForm(forms.ModelForm):

    class Meta:
        model = Newsletter
        exclude = ('joined_date',)
        fields=('email',)


