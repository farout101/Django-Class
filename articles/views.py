from django.shortcuts import render
from .models import Article
# Create your views here.
def article_detail_view(request, id=None):
    
    print("This is from article_detail_view")
    
    article = None
    
    if id is not None:
        article = Article.objects.get(id=id)
    
    context = {
        "object" : article
    }
    
    return render(request, "articles/detail.html", context=context)

def article_search_view(request):

    print("This is from article_search_view")

    query_dict = request.GET
    
    try:
        query = int(query_dict.get("q"))
    except:
        query = None
    
    article_obj = None
    
    if query is not None:
        article_obj = Article.objects.get(id=query)
    
    context = {
        "object" : article_obj
    }

    return render(request, "articles/search.html", context=context)

def article_create_view(request):
    
    print("This is from article_create_view")
    
    context = {}
    
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        print(f"title: {title}, content : {content}")
        object = Article.objects.create(title=title, content=content)
        context['object'] = object
        context['created'] = True
    
    return render(request, "articles/create.html", context=context)
