from django import forms
from .models import StudentRegistration

class User(forms.ModelForm):
    class Meta:
        model = StudentRegistration
        fields = '__all__'   # All Fields came from StudentRegistration 
        # fields = ['name', 'email', 'password']
        widgets = {
            'password':forms.PasswordInput,
            'name':forms.TextInput,
        }