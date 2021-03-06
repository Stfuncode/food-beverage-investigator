from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, UsernameField

from account.models import Account

class loginForm(AuthenticationForm):
    remember_me = forms.BooleanField(
        label=("Remember Me"), initial=False, required=False
    )
    username = UsernameField(label="", widget=forms.TextInput(
        attrs={'placeholder': 'Username', 'name': 'txt', 'class': 'mb-3'}
    ))
    password = forms.CharField(label="", widget=forms.TextInput(
        attrs={'placeholder': 'Password', 'name': 'pswd', 'class': 'mb-4', 'type': 'password'}
    ))


class createUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Username"}))
    name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Full Name"}), 
        label="Full Name",
    )
    email = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Email"}))
    contact_number = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Contact Number"}),
        label="Contact Number",
    )
    class Meta:
        model = Account
        fields = ("username","name","email","contact_number")

class viewUserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Username","disabled": "disabled"}))
    name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Full Name.","disabled": "disabled"}), 
        label="Full Name",
    )
    email = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Email.","disabled": "disabled"}))
    contact_number = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Please enter contact number.","disabled": "disabled"}),
        label="Contact Number",
    )
    class Meta:
        model = Account
        fields = ("username","name","email","contact_number")

class editUserForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Username"}))
    name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Full Name."}), 
        label="Full Name",
    )
    email = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Email."}))
    contact_number = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Please enter contact number."}),
        label="Contact Number",
    )
    class Meta:
        model = Account
        fields = ("username","name","email","contact_number")