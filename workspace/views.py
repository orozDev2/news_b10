from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required as _login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from news.models import News
from workspace.decorators import login_required, is_owner
from workspace.forms import NewsForm


@login_required(url='/login/')
def workspace(request):
    news = News.objects.filter(author=request.user).order_by('-date', 'name')
    page = request.GET.get('page', 1) or 1
    pagin = Paginator(news, 12)
    news = pagin.get_page(page)

    return render(request, 'workspace/index.html', {'news': news})


@login_required()
def create_news(request):

    form = NewsForm()

    if request.method == 'POST':
        form = NewsForm(data=request.POST, files=request.FILES)

        if form.is_valid():
            news = form.save()
            return redirect('/workspace/')

    return render(request, 'workspace/create_news.html', {'form': form})


@login_required()
@is_owner
def update_news(request, id):

    if not request.user.is_authenticated:
        return redirect('/')

    news = get_object_or_404(News, id=id)
    form = NewsForm(instance=news)

    if request.method == 'POST':
        form = NewsForm(data=request.POST, files=request.FILES, instance=news)

        if form.is_valid():
            form.save()
            return redirect('/workspace/')

    return render(request, 'workspace/update_news.html', {'form': form, 'news': news})


@login_required()
@is_owner
def delete_news(request, id):
    news = get_object_or_404(News, id=id)
    news.delete()
    return redirect('/workspace/')


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
