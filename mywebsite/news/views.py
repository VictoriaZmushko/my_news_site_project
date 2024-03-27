from django.shortcuts import render
from django.shortcuts import get_object_or_404

# Create your views here.
from .models import Article


def article_list(request, id):
    article = get_object_or_404(article, id=id)
    return render(request, "news/article/list.html", {"article": article})


def article_list(request):
    articles = Article.published.all()
    return render(request, "news/article/list.html", {"articles": articles})
