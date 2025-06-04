from django.shortcuts import render, get_object_or_404
from django.views import View

from hexlet_django_blog.article.models import Article


class ArticleView(View):
    def get(self, request, tags, article_id):
        article = get_object_or_404(Article, id=article_id)
        return render(request, "articles/article.html", {"article": article})


class IndexView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(
            request,
            "articles/index.html",
            context={
                "articles": articles,
            },
        )