from django import forms

from cities.models import City


class HtmlForm(forms.Form):
    name = forms.CharField(label="Shahar")


class CityForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Shahar nomini kiriting"}))

    class Meta:
        model = City
        fields = ('name', )

    def clean_name(self):
        name = self.cleaned_data['name']
        try:
            city = City.objects.get(name=name)
        except:
            city = None
        if city:
            raise forms.ValidationError('Bu shahar allaqachon kiritilgan!')


        return name
