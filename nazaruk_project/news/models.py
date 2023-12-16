from django.db import models
from django.urls import reverse

# Create your models here.
# in models.py
NEWS_CATEGORIES = [
    ('POLITICS', 'Politics'),
    ('WEATHER', 'Weather'),
    ('UK', 'UK'),
    ('USA', 'USA'),
    ('SPORTS', 'Sports'),
    ('EUROPE', 'Europe'),
    ('SCIENCE', 'Science'),
    ('TECH', 'Tech'),
    # Add more categories as needed
]

class News(models.Model):
    title = models.CharField("Title of news", max_length=100, null=True)
    intro = models.CharField("Introduction", max_length=250, null=True)
    full_text = models.TextField('Full text of article', null=True)
    date = models.DateTimeField("Date of publication", null=True)
    category = models.CharField(max_length=10, choices=NEWS_CATEGORIES, null=True)

    def get_absolute_url(self):
        return reverse('news-detail', args=[str(self.id)])
