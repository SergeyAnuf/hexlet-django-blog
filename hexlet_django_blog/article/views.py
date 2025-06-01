from django.http import HttpResponse

def index(request, tags, article_id):
    return HttpResponse(f"Статья номер {article_id}. Тег {tags}")