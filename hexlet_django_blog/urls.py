"""
URL configuration for hexlet_django_blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, reverse
from django.shortcuts import redirect
from hexlet_django_blog import views

# Функция для редиректа с домашней страницы
def home_redirect(request):
    # Используем существующую статью или создаем по умолчанию
    try:
        # Пытаемся получить первую статью
        first_article = Article.objects.first()
        if first_article:
            article_url = reverse('article', kwargs={
                'tags': 'python', 
                'article_id': first_article.id
            })
            return redirect(article_url)
    except:
        pass
    
    # Если статей нет - редиректим на список статей
    return redirect('articles_index')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_redirect, name='index'),  # Редирект с главной
    path("about/", views.about, name='about'),
    path("articles/", include("hexlet_django_blog.article.urls")),
]
