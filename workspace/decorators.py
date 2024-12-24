from django.shortcuts import redirect, get_object_or_404

from news.models import News


# def login_required(func):
#
#     def inner_func(request, *args, **kwargs):
#         if not request.user.is_authenticated:
#             return redirect('/')
#
#         return func(request, *args, **kwargs)
#
#     return inner_func


def login_required(url='/login/'):

    def decorator(func):

        def inner_func(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect(url)

            return func(request, *args, **kwargs)

        return inner_func

    return decorator


def is_owner(func):
    def inner_func(request, *args, **kwargs):
        user = request.user
        news = get_object_or_404(News, id=kwargs.get('id'))

        if news.author != user:
            return redirect('/workspace/')

        return func(request, *args, **kwargs)

    return inner_func