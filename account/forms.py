from operator import attrgetter
from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm
from django.shortcuts import get_object_or_404

from .models import UserBase


class RegistrationForm(forms.ModelForm):

    user_name = forms.CharField(label='Enter Username', min_length=4, max_length=50, help_text='Required')
    email = forms.EmailField(max_length=100, help_text='Required', error_messages={'required': 'Sorry, you will need an email'})
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = UserBase
        fields = ('user_name', 'email', )
    
    def clean_username(self):
        user_name = self.cleaned_data['user_name'].lower()
        r = UserBase.objects.filter(user_name=user_name)
        if r.count():
            raise forms.ValidationError('Foydalanuvchi nomi band!')
        return user_name

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Password do not match!')
        return cd['password2']

    def clean_eamil(self):
        email = self.cleaned_data['email']
        if UserBase.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'Please use another Email, that is already taken')
        return email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_name'].widget.attrs.update(
            {"class": "form-control mb-3", "placeholder": "Username"})
        self.fields['email'].widget.attrs.update(
            {"class": "form-control mb-3", "placeholder": "E-mail", "name": "email"})
        self.fields['password'].widget.attrs.update(
            {"class": "form-control mb-3", "placeholder": "Password"})
        self.fields['password2'].widget.attrs.update(
            {"class": "form-control", "placeholder": "Repeat password"}
        )





class UserLoginForm(AuthenticationForm):

    user_name = forms.CharField(label='Username', widget=forms.TextInput(attrs={
        "class": "form-control mb-3",
        "placeholder": "Usernameni kiriting"}))

    password = forms.CharField(label='Parol', widget=forms.PasswordInput(attrs={
        "class": "form-control mb-3",
        "placeholder": "Parolni kiriting"}))

    class Meta:
        models = UserBase
        fields = ('user_name', 'password')


class PwdResetForm(PasswordResetForm):

    email = forms.EmailField(max_length=254, widget=forms.TextInput(
        attrs={"class": "form-control mb-3", "placeholder": "Emailingizni kiriting", "id": "form-email"}))

    def clean_email(self):
        email = self.cleaned_data['email']
        u = UserBase.objects.filter(email=email)
        if not u:
            raise forms.ValidationError("Bunday email bilan ro'yhatdan o'tgan foydalanuvchi mavjud emas!")
        return email



class PwdResetConfirmForm(SetPasswordForm):

    new_password1 = forms.CharField(
        label='Yangi parol', widget=forms.PasswordInput(
            attrs={"class": "form-control mb-3", "placeholder": "Yangi parol", "id": "form-newpass"}))
    new_password2 = forms.CharField(
        label='Parolni tasdiqlang', widget=forms.TextInput(
            attrs={"class": "form-control mb-3", "placeholder": "Parolni tasdiqlang", "id": "form-newpass2"}))



class UserEditForm(forms.ModelForm):

    email = forms.EmailField(
        label="Email (o'zgartirib bo'lmaydi)", max_length=200, widget=forms.TextInput(
            attrs={"class": "form-control mb-3", "placeholder": "email", "id": "form-email", "readonly": "readonly"}))
    user_name = forms.CharField(
        label='Foydalanuvchi nomi', min_length=4, max_length=50, widget=forms.TextInput(
            attrs={"class": "form-control mb-3", "placeholder": "Forydalanuvchi nomi", "id": "form-username", "readonly": "readonly"}))
    first_name = forms.CharField(
        label='Ism', min_length=4, max_length=50, widget=forms.TextInput(
            attrs={"class": "form-control mb-3", "placeholder": "Ism", "id": "form-lastname"}))

    class Meta:
        model = UserBase
        fields = ['email', 'user_name', 'first_name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['user_name'].required = True
