from django import forms
from cities.models import City

from trains.models import Train


class TrainForm(forms.ModelForm):
    name = forms.CharField(label='Poyezd nomeri', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Poyezd nomerini kiriting'
    }))
    travel_time = forms.IntegerField(label="Yo'l vaqti", widget=forms.NumberInput(attrs={
        'class': 'form-control', "placeholder": "Yo'l vaqtini kiriting"}))

    from_city = forms.ModelChoiceField(
        label='Qayerdan', queryset=City.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}))

    to_city = forms.ModelChoiceField(
        label='Qayerga', queryset=City.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Train
        fields = ('__all__')
