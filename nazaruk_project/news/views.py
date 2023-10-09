from django.shortcuts import render
from .models import Article
from .forms import ArticlesForm

def news_home(request):
    news = Article.objects.all().order_by("-date")[:]
    return render(request, 'news/news_home.html', {'news' : news})

def create(request):
    error = ''
    if request.method == "POST":
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Error(form was incorrect)'

    form = ArticlesForm()

    data = {
        'form' : form,
        'error' : error
    }
    return render(request, 'news/create.html', data)
