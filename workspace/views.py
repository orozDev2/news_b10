from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required as _login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from news.models import News
from workspace.decorators import login_required, is_owner
from workspace.forms import NewsForm
from django.contrib import messages


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
            news = form.save(commit=False)
            news.author = request.user
            news.save()
            messages.success(request, f'The news "{news.name}" was created successfully.')
            return redirect('/workspace/')

        messages.error(request, 'Please correct errors')

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
            messages.error(request, f'The news "{news.name}" was updated successfully.')
            return redirect('/workspace/')

        messages.error(request, 'Please correct errors')

    return render(request, 'workspace/update_news.html', {'form': form, 'news': news})


@login_required()
@is_owner
def delete_news(request, id):
    news = get_object_or_404(News, id=id)
    news.delete()
    messages.success(request, f'The news "{news.name}" was deleted successfully.')
    return redirect('/workspace/')
