from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from cities.models import City
from . import forms


def home(request, pk=None):
    if request.method == 'POST':
        form = forms.CityForm(request.POST)
        if form.is_valid():
            form.save()
    form = forms.CityForm()
    title = "Shaharlar ro'yhati"
    qs = City.objects.all()
    context = {
        "title": title,
        "objects_list": qs,
        "form": form,
        }
    return render(request, 'cities/home.html', context)



class CityDetailView(DetailView):
    queryset = City.objects.all()
    template_name = 'cities/detail.html'



class CityCreateView(CreateView):
    model = City
    form_class = forms.CityForm
    template_name = 'cities/create.html'
    success_url = reverse_lazy('cities:home')



class CityUpdateView(UpdateView):
    model = City
    form_class = forms.CityForm     
    template_name = 'cities/update.html'
    success_url = reverse_lazy('cities:home')



class CityDeleteView(DeleteView):
    model = City
    template_name = 'cities/delete.html'
    success_url = reverse_lazy('cities:home')

    # Ogohlantirishsiz o'chirish
    # def get(self, request, *args, **kwargs):
    #     return self.post(request, *args, **kwargs)
