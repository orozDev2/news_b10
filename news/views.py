from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from news.models import News, Category


def main(request):
    news = News.objects.filter(is_published=True).order_by('-date', 'name')

    category_id = request.GET.get('category')
    if category_id is not None:
        news = news.filter(category__id=int(category_id))

    search = request.GET.get('search')
    print(search)

    if search is not None:
        news = news.filter(name__icontains=search)

    page = request.GET.get('page', 1) or 1
    pagin = Paginator(news, 12)
    news = pagin.get_page(page)

    return render(request, 'index.html', {'news': news})


def about(request):
    return render(request, 'about.html')


def detail_news(request, id):
    news = get_object_or_404(News, id=id)
    news.views += 1
    news.save()
    return render(request, 'detail_news.html', {'news': news})


# Create your views here.