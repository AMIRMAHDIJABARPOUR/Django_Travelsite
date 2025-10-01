from captcha.fields import CaptchaField
from django import forms
from .models import Comment

class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('approved_by ','create_date ')
        fields =['name','email','subject','massage']