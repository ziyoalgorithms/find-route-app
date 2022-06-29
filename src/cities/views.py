from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.core.paginator import Paginator
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from cities.models import City
from . import forms


def home(request, pk=None):
    title = "Shaharlar ro'yhati"
    if request.method == "POST":
        form = forms.CityForm(request.POST)
        if form.is_valid():
            form.save
    form = forms.CityForm()
    qs = City.objects.all()
    list = Paginator(qs, 5)
    page_number = request.GET.get('page')
    page_obj = list.get_page(page_number)
    context = {
        "title": title,
        "form": form,
        "page_obj": page_obj,
        }
    
    return render(request, 'cities/home.html', context)



class CityDetailView(DetailView):
    queryset = City.objects.all()
    template_name = 'cities/detail.html'



class CityCreateView(SuccessMessageMixin, CreateView):
    model = City
    form_class = forms.CityForm
    template_name = 'cities/create.html'
    success_url = reverse_lazy('cities:home')
    success_message = "Shahar muvaffaqqiyatli qo'shildi!"




class CityUpdateView(SuccessMessageMixin, UpdateView):
    model = City
    form_class = forms.CityForm     
    template_name = 'cities/update.html'
    success_url = reverse_lazy('cities:home')
    success_message = "Shahar haqidagi ma'lumotlar muvaffaqqiyatli tahrirlandi!"



class CityDeleteView(SuccessMessageMixin, DeleteView):
    model = City
    # template_name = 'cities/delete.html'
    success_url = reverse_lazy('cities:home')


    def get(self, request, *args, **kwargs):
        messages.success(request, "Shahar muvaffaqqiyatli o'chirildi!")
        return self.delete(request, *args, **kwargs)
