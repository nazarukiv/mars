from .models import Article
from django.forms import ModelForm

class ArticlesForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'anons', 'full_text', 'date']


