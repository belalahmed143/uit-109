from django import forms
from .models import *


class ContactForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':"Name"
    }))
    phone = forms.CharField(widget=forms.NumberInput(attrs={
        'class':'form-control',
        'type':'tel',
        'placeholder':"phone"
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder':"email"
    }))
    subject = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':"subject",
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class':'form-control',
        'rows': 3,
        'placeholder':"message"
    }))
    class Meta:
        model = Contact
        fields = ['name','phone','email','subject','message']

class NewsLetterForm(forms.ModelForm):
    class Meta:
        model = NewsLetter
        fields = ['email']

class StudentAddForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'