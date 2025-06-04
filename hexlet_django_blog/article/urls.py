from django.urls import path

from hexlet_django_blog.article.views import IndexView, ArticleView

urlpatterns = [
    path("", IndexView.as_view(), name='articles_index'),
    # Добавьте новый маршрут для отдельных статей
    path("<str:tags>/<int:article_id>/", ArticleView.as_view(), name='article'),
]