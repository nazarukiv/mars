from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    data = {
        "title": "About This Project",
        'values' : ['Example', 'OF', 'Values'],
        'obj' : {
            'car' : 'Mercedes',
            'age' : 17,
            'hobby' : 'gym and boxing'
        }
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')

def ivan(request):
    return HttpResponse("<h4>Checking of work.My name is Ivan Nazaruk</h4>")

