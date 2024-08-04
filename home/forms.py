from django import forms
from .models import Person
from django.contrib.auth.hashers import make_password

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
     
    class Meta:
        model = Person
        fields = ['username', 'password', 'person_id', 'first_name', 'last_name', 'phone', 'school_name', 'study', 'degree', 'gpa']

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.password = make_password(self.cleaned_data['password'])
        if commit:
            instance.save()
        return instance


class LoginPage(forms.Form):
    user_name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    