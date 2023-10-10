from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticlesForm
from django.views.generic import DetailView, ListView, UpdateView, DeleteView


def news_home(request):
    news = Article.objects.all().order_by("-date")[:]
    return render(request, 'news/news_home.html', {'news' : news})


class NewsDeleteView(DeleteView):
    model = Article
    success_url = '/news/'
    template_name = 'news/news-delete.html'

class NewsUpdateView(UpdateView):
    model = Article
    template_name = 'news/create.html'

    form_class = ArticlesForm

class NewsDetailView(DetailView):
    model = Article
    template_name = 'news/details_view.html'
    context_object_name = 'article'


def create(request):
    error = ''
    if request.method == "POST":
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Error(form was incorrect)'

    form = ArticlesForm()

    data = {
        'form' : form,
        'error' : error
    }
    return render(request, 'news/create.html', data)
