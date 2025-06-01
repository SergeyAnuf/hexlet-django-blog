from django.urls import path
from .views import index  # Импортируем нашу функцию index

urlpatterns = [
    # Новый маршрут для статей с параметрами
    path('<str:tags>/<int:article_id>/', index, name='article'),
]
