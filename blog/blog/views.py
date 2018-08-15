from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

from .models import Theme, Post


def index(request):
    themes_list = Theme.objects.all()
    last_post_list = Post.objects.order_by('-publication_date')[:5]
    context = {'themes_list': themes_list,
               'post_list': last_post_list,
               }
    return render(request, 'blog/index.html', context)


def over_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)

    if user is not None:
        try:
            login(request, user)
        except Exception:
            return HttpResponse('Login failed!')
        else:
            return HttpResponse('Login success!')
    else:
        return HttpResponse('User does not exist!')


def over_logout(request):
    logout(request)
    return HttpResponse('Logout complete!')