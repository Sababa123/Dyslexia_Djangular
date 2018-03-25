from django import forms
from .models import Patient
from .validation import validate_pname
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

# class PatientCreateForm(forms.Form):
    
#     p_name = forms.CharField()
#     p_dob = forms.DateField( required = False )



class Patient_classCreateForm(forms.ModelForm):

    # p_name = forms.CharField(validators =[validate_pname] ) #required=false

    class Meta:
        model = Patient
        fields = [
            'first_name',
            'last_name',
            'age',
            'p_dob',
            'school',
            'grade',
            'password',
            'p_email',
        ]

class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email',)

    def send_activation_mail(self):
        pass

    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email__iexact=email)
        if qs.exists():
            raise forms.ValidationError("Cannot use this email. It's already registered")
        return email

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_active = False
        # create a new user hash for activating email.

        if commit:
            user.save()
            
        return user

