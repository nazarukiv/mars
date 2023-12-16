from django.contrib import admin
from django.utils.text import Truncator
from .models import News

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'intro', 'truncated_full_text', 'date', 'category')

    # This is the method to truncate the full_text content
    def truncated_full_text(self, obj):
        return Truncator(obj.full_text).chars(50)
    truncated_full_text.short_description = 'Truncated Full Text'

admin.site.register(News, NewsAdmin)
