from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import News
from .forms import NewsForm

# Create your views here.
def Homepage(request):
    return render(request, 'news/index.html')


def all_News(request):
    News_list = News.objects.all()
    context = {'News_list': News_list}
    return render(request, 'news/news_page.html', context)



def single_news(request, news_id):
    current_news = News.objects.get(id=news_id)
    context = {'news': current_news}
    return render(request, 'news/single_news.html', context)



def create_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('news')
        else:
            return HttpResponse("Something isn't right")
    else:
        form = NewsForm()
    return render(request, 'news/create.html', {'form': form})


def Contactpage(request):
    return render(request, "news/contact.html")