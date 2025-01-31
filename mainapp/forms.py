from django import forms
from django.core.validators import EmailValidator

from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'phone', 'subject', 'message')
        exclude = ('when_sent', 'replied', 'when_replied')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
        }
  
    # name = forms.CharField(max_length=100, required=True)
    # email = forms.CharField(validators=[EmailValidator()], required=True)
    # phone = forms.CharField(max_length=15, required=True)
    # subject = forms.CharField(max_length=100, required=True)
    # message = forms.CharField(widget=forms.Textarea, required=True)