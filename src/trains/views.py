from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    ListView
    )
from django.urls import reverse_lazy, reverse
from django.core.paginator import Paginator
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from trains.models import Train
from trains.forms import TrainForm


def home(request, pk=None):
    title = "Poyezd ro'yhati"
    qs = Train.objects.all()
    list = Paginator(qs, 5)
    page_number = request.GET.get('page')
    page_obj = list.get_page(page_number)
    context = {
        "title": title,
        "page_obj": page_obj,
        }
    
    return render(request, 'trains/home.html', context)



class TrainListView(ListView):
    paginate_by = 5
    model = Train
    template_name = 'trains/home.html'



class TrainDetailView(DetailView):
    queryset = Train.objects.all()
    template_name = 'trains/detail.html'



class TrainCreateView(SuccessMessageMixin, CreateView):
    model = Train
    form_class = TrainForm
    template_name = 'trains/create.html'
    success_url = reverse_lazy('trains:home')
    success_message = "Poyezd muvaffaqqiyatli qo'shildi!"




class TrainUpdateView(SuccessMessageMixin, UpdateView):
    model = Train
    form_class = TrainForm     
    template_name = 'trains/update.html'
    success_url = reverse_lazy('trains:home')
    success_message = "Poyezd haqidagi ma'lumotlar muvaffaqqiyatli tahrirlandi!"



class TrainDeleteView(SuccessMessageMixin, DeleteView):
    model = Train
    template_name = 'trains/delete.html'
    success_url = reverse_lazy('trains:home')


    def get(self, request, *args, **kwargs):
        messages.success(request, "Poyezd muvaffaqqiyatli o'chirildi!")
        return self.delete(request, *args, **kwargs)
