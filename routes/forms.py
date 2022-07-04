from cProfile import label
from django import forms

from cities.models import City
from trains.models import Train
from routes.models import Route


class RouteForm(forms.Form):

    from_city = forms.ModelChoiceField(
        label='Qayerdan', queryset=City.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control js-example-basic-single'})
    )

    to_city = forms.ModelChoiceField(
        label='Qayerga', queryset=City.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control js-example-basic-single'})
    )
    
    cities = forms.ModelMultipleChoiceField(
        label='Qaysi shaharlar orqali',
        queryset=City.objects.all(),
        required=False,
        widget=forms.SelectMultiple(
            attrs={'class': 'form-control js-example-basic-multiple'})
    )

    travelling_time = forms.IntegerField(label="Yo'l vaqti", widget=forms.NumberInput(attrs={
        'class': 'form-control', "placeholder": "Yo'l vaqtini kiriting"})
    )


class RouteModelForm(forms.ModelForm):

    name = forms.CharField(label='Marshrut nomi', widget=forms.TextInput(attrs={
        "class": "form-control", "placeholder": "Marshrut nomini kiriting"}))

    from_city = forms.ModelChoiceField(
        queryset=City.objects.all(), widget=forms.HiddenInput())

    to_city = forms.ModelChoiceField(
        queryset=City.objects.all(), widget=forms.HiddenInput())
    
    trains = forms.ModelMultipleChoiceField(
        queryset=Train.objects.all(),
        required=False, widget=forms.SelectMultiple(
                            attrs={'class': 'form-control d-none'}))

    travel_times = forms.IntegerField(widget=forms.HiddenInput())


    class Meta:
        model = Route
        fields = '__all__'
