from django import forms
from django.core.validators import EmailValidator


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.CharField(validators=[EmailValidator()])
    phone = forms.CharField(max_length=50)
    subject = forms.CharField(max_length=250)
    message = forms.CharField(widget=forms.Textarea)
