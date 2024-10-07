from django.shortcuts import render
from django.http import JsonResponse
from .script import scrape_imdb_news
from .models import News
# Create your views here.
def run_scrapper(request):
    scrape_imdb_news()
    return JsonResponse({
        'status': 'success', 
        'message': '"News scraped successfully!"'
        
    })


def index(request):
    news = News.objects.all()
    context = {
        'news': news
    }
    return render(request, 'index.html', context)
