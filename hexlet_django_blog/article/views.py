from django.views import View
from django.shortcuts import render

class ArticleIndexView(View):
    template_name = 'articles/index.html'  # Можно вынести в атрибут класса
    
    def get(self, request, *args, **kwargs):
        context = {'app_name': 'Articles'}  # Формируем контекст
        return render(request, self.template_name, context)