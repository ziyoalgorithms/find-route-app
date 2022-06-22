from django.http import HttpResponse
from django.shortcuts import render



def home(request):
    title = "bosh sahifa"
    name = 'Ziyodullokhon'

    content = {
        "title": title,
        "name": name,
    }

    return render(request, 'home.html', content)



def about(request):
    title = 'about'
    name = 'Biz haqimizda'

    content = {
        "title": title,
        "name": name,
    }

    return render(request, 'about.html', content)
