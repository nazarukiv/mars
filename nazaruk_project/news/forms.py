from .models import Article
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'intro', 'full_text', 'date']

        widgets = {
            "title" : TextInput(attrs={
                "class" : "form-control",
                "placeholder" : "Name of Article"
            }),
            "intro": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Introduction"
            }),
            "date": DateTimeInput(attrs={
                "class": "form-control",
                "placeholder": "Date of publication"
            }),
            "full_text": Textarea(attrs={
                "class": "form-control",
                "placeholder": "Text of article"
            })
        }
