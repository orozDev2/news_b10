from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from news.models import News
from workspace.forms import NewsForm


def workspace(request):

    if not request.user.is_authenticated:
        return redirect('/')

    news = News.objects.filter(author=request.user).order_by('-date', 'name')
    page = request.GET.get('page', 1) or 1
    pagin = Paginator(news, 12)
    news = pagin.get_page(page)

    return render(request, 'workspace/index.html', {'news': news})


def create_news(request):
    form = NewsForm()

    if request.method == 'POST':
        form = NewsForm(data=request.POST, files=request.FILES)

        if form.is_valid():
            news = form.save()
            return redirect('/workspace/')

    return render(request, 'workspace/create_news.html', {'form': form})


def update_news(request, id):
    news = get_object_or_404(News, id=id)
    form = NewsForm(action=NewsForm.UPDATE, initial={
        'name': news.name,
        'description': news.description,
        'content': news.content,
        'author': news.author,
        'category': news.category,
        'tags': news.tags.all(),
        'is_published': news.is_published,
    })

    if request.method == 'POST':
        form = NewsForm(data=request.POST, files=request.FILES, action=NewsForm.UPDATE)

        if form.is_valid():
            image = form.cleaned_data.pop('image')
            tags = form.cleaned_data.pop('tags')

            news.tags.clear()
            news.tags.add(*tags)

            if image is not None:
                news.image.save(image.name, image)

            news.save()

            News.objects.filter(id=id).update(**form.cleaned_data)

            return redirect('/workspace/')

    return render(request, 'workspace/update_news.html', {'form': form, 'news': news})


# def update_news(request, id):
#
#     news = get_object_or_404(News, id=id)
#
#     if request.method == 'POST':
#         news.name = request.POST.get('name')
#         news.description = request.POST.get('description')
#         news.content = request.POST.get('content')
#         news.author = request.POST.get('author')
#         news.category = Category.objects.get(id=int(request.POST.get('category')))
#
#         tags_id = list(map(int, request.POST.getlist('tags')))
#         tags = Tag.objects.filter(id__in=tags_id)
#         news.tags.clear()
#         news.tags.add(*tags)
#
#         image = request.FILES.get('image')
#         if image is not None:
#             news.image.save(image.name, image)
#
#         news.save()
#
#         return redirect('/workspace/')
#
#     categories = Category.objects.all()
#     tags = Tag.objects.all()
#     return render(request, 'workspace/update_news.html', {'categories': categories, 'tags': tags, 'news': news})

# Create your views here.
