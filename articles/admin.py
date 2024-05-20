from django.contrib import admin

# Register your models here.
from .models import Article

#custom admin view
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content']
    search_fields = ['id', 'title']

admin.site.register(Article, ArticleAdmin) # can adjust the admin view 