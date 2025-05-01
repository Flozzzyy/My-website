from django.shortcuts import render
from .models import Articles
from .forms import ArticlesForm
# Create your views here.


def news_home(request):
    news = Articles.objects.order_by('-data')
    return render(request, 'news/news_home.html', {"news":news})

def create(request):
    form = ArticlesForm
    data = {
        'form': form
    }
    return render(request, 'news/create.html', data)
