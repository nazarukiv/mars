from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField("Title of news", max_length=100)
    intro = models.CharField("Introduction", max_length=250)
    full_text = models.TextField('Full text of article')
    date = models.DateTimeField("Date of publication")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "News"
        verbose_name_plural = 'News'
