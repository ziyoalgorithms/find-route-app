from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.hashers import check_password

User = get_user_model()


class UserLoginForm(forms.Form):

    username = forms.CharField(label='username', widget=forms.TextInput(attrs={
        "class": "form-cotrol",
        "placeholder": "Usernameni kiriting"}))

    password = forms.CharField(label='username', widget=forms.PasswordInput(attrs={
        "class": "form-cotrol",
        "placeholder": "Parolni kiriting"}))


    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            qs = User.objects.filter(username=username)
            if not qs.exists():
                raise forms.ValidationError('Bunday foydalanuvchi mavjud emas!')
            if not check_password(password, qs[0].password):
                raise forms.ValidationError("Parol noto'g'ri kiritildi!")
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('Bu foydalanuvchi faol emas!')
        return super().clean(*args, **kwargs)            


class UserRegistrationForm(forms.ModelForm):

    username = forms.CharField(label='Isminizni kiriting', widget=forms.TextInput(attrs={
        "class": "form-cotrol",
        "placeholder": "Usernameni kiriting"}))

    password = forms.CharField(label='Parolni kiriting', widget=forms.PasswordInput(attrs={
        "class": "form-cotrol",
        "placeholder": "Parolni kiriting"}))
    
    password2 = forms.CharField(label='Parolni tasdiqlang', widget=forms.PasswordInput(attrs={
        "class": "form-cotrol",
        "placeholder": "Parolni tasdiqlang"}))


    class Meta:
        model = User
        fields = ('username', )

    def clean_password2(self):
        data = self.cleaned_data
        if data['password'] != data['password2']:
            raise forms.ValidationError('Parollar bir-biriga mos emas!')
