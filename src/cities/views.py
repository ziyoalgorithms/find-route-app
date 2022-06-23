from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView

from cities.models import City


def home(request, pk=None):

    if pk:
        title = "Shahar"
        city = get_object_or_404(City, id=pk)
        context = {
        "title": title,
        "object": city,
        }
        return render(request, 'cities/detail.html', context)

    title = "Shaharlar ro'yhati"
    qs = City.objects.all()
    context = {
        "title": title,
        "objects_list": qs,
        }
    return render(request, 'cities/home.html', context)



class CityDetailView(DetailView):
    queryset = City.objects.all()
    template_name = 'cities/detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'shahar haqida'
        return context
