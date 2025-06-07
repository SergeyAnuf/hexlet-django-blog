from django.urls import path

from hexlet_django_blog.article.views import (
    IndexView, 
    ArticleView, 
    ArticleFormCreateView, 
    ArticleFormEditView,
)

urlpatterns = [
    path("", IndexView.as_view(), name='articles_index'),
    # Добавьте новый маршрут для отдельных статей
    path("<int:id>/", ArticleView.as_view(), name='article_show'),
    # Маршрут для добавления статей
    path("create/", ArticleFormCreateView.as_view(), name="articles_create"),
    # Маршрут для обновления статьи
    path("<int:id>/edit/", ArticleFormEditView.as_view(), name="articles_update"),
]