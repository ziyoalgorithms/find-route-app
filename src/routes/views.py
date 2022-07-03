from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import ListView, DetailView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin



from routes.models import Route
from routes.forms import RouteForm, RouteModelForm
from routes.utils import get_routes
from trains.models import Train
from cities.models import City


def home(request):
    title = 'Marshrutlar'
    form = RouteForm()
    context = {
        'title': title,
        'form': form
    }
    return render(request, 'routes/home.html', context)


def find_routes(request):
    if request.method == "POST":
        form = RouteForm(request.POST)
        if form.is_valid():
            try:
                context = get_routes(request, form)
            except ValueError as e:
                messages.error(request, e)
                return render(request, 'routes/home.html', {"form": form})
            return render(request, 'routes/home.html', context)

        return render(request, 'routes/home.html', {'form': form})

    else:
        form = RouteForm()
        messages.error(request, "Qidirish uchun ma'lumot kiriting!")
        return render(request, 'routes/home.html', {'form': form})



def add_route(request):
    if request.method == "POST":
        context = {}
        data = request.POST
        if data:
            total_time = int(data['total_time'])
            from_city_id = int(data['from_city'])
            to_city_id = int(data['to_city'])
            trains = data['trains'].split(',')
            trains_list = [int(t) for t in trains if t.isdigit()]
            qs = Train.objects.filter(id__in=trains_list).select_related('from_city', 'to_city')
            cities = City.objects.filter(id__in=[from_city_id, to_city_id]).in_bulk()
            form = RouteModelForm(initial={
                                            'from_city': cities[from_city_id],
                                            'to_city': cities[to_city_id],
                                            'travel_times': total_time,
                                            'trains': qs})
        context['form'] = form

        return render(request, 'routes/create.html', context)

    else:
        form = RouteForm()
        messages.error(request, "Mavjud bo'lmagan marshrutni saqlab bo'lmaydi!")
        return redirect('/')



def save_route(request):
    if request.method == "POST":
        form = RouteModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Marshrut saqlandi!")
            return redirect('/')
        return render(request, 'routes/create.html', {'form': form})

    else:
        form = RouteForm()
        messages.error(request, "Mavjud bo'lmagan marshrutni saqlab bo'lmaydi!")
        return redirect('/')




class RouteListView(ListView):
    paginate_by = 5
    model = Route
    template_name = 'routes/list.html'




class RouteDetailView(DetailView):
    queryset = Route.objects.all()
    template_name = 'routes/detail.html'



class RouteDeleteView(LoginRequiredMixin, DeleteView):
    model = Route
    success_url = reverse_lazy('list')


    def get(self, request, *args, **kwargs):
        messages.success(request, "Marshrut muvaffaqqiyatli o'chirildi!")
        return self.delete(request, *args, **kwargs)