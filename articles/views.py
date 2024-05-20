from django.shortcuts import render
from .models import Article
# Create your views here.
def article_detail_view(request, id=None):
    
    article = None
    
    if id is not None:
        article = Article.objects.get(id=id)
    
    context = {
        "object" : article
    }
    
    return render(request, "articles/detail.html", context=context)