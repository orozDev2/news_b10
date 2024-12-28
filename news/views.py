from django.contrib.auth import login, authenticate, logout
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect

from news.filters import NewsFilter
from news.forms import LoginForm
from news.models import News


def main(request):
    news = News.objects.filter(is_published=True).order_by('-date', 'name')

    category_id = request.GET.get('category')
    if category_id is not None:
        news = news.filter(category__id=int(category_id))

    search = request.GET.get('search')

    if search is not None:
        news = news.filter(name__icontains=search)

    filterset = NewsFilter(data=request.GET, queryset=news)

    news = filterset.qs

    page = request.GET.get('page', 1) or 1
    pagin = Paginator(news, 12)
    news = pagin.get_page(page)

    return render(request, 'index.html', {'news': news, 'filterset': filterset})


def about(request):
    return render(request, 'about.html')


def detail_news(request, id):
    news = get_object_or_404(News, id=id)
    news.views += 1
    news.save()
    return render(request, 'detail_news.html', {'news': news})


def login_profile(request):
    if request.user.is_authenticated:
        return redirect('/')

    form = LoginForm()
    message = None

    if request.method == 'POST':
        form = LoginForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            # user = User.objects.filter(username=username).first()
            # if user and user.check_password(password):
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)

                return redirect('/workspace/')

            message = 'The user is not found or the password is incorrect.'

    return render(request, 'auth/login.html', {'form': form, 'message': message})


def logout_profile(request):
    if request.user.is_authenticated:
        logout(request)

    return redirect('/')

# Create your views here.
