import random
from django.http import HttpResponse
from articles.models import Article
from django.template.loader import render_to_string

def home_view(request):
    
    number = random.randint(1,4)
    
    article = Article.objects.get(id=number)
    
    article_qs = Article.objects.all()
    
    context = {
        "article_qs" : article_qs,
        "title" : article.title,
        "id" : article.id,
        "content" : article.content,
    }
    
    HTTP_STRING = render_to_string("home-view.html",context=context)
    
    return HttpResponse(HTTP_STRING)