from django.shortcuts import render, redirect
from .models import News
from .forms import ArticlesForm
from django.views.generic import DetailView, ListView, UpdateView, DeleteView
from django.urls import reverse




class NewsDeleteView(DeleteView):
    model = News
    success_url = '/news/'
    template_name = 'news/news-delete.html'

class NewsUpdateView(UpdateView):
    model = News
    template_name = 'news/create.html'

    form_class = ArticlesForm

    def get_success_url(self):
        return reverse('news_home')

class NewsDetailView(DetailView):
    model = News
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

# in views.py
def news_home(request, category=None):
    if category:
        news = News.objects.filter(category=category.upper())
    else:
        news = News.objects.all()
    return render(request, 'news/news_home.html', {'news': news})

