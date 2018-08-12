from django.shortcuts import render

from .models import Theme, Post


def index(request):
    themes_list = Theme.objects.all()
    last_post_list = Post.objects.order_by('-publication_date')[:5]
    context = {'themes_list': themes_list,
               'post_list': last_post_list,
               }
    return render(request, 'blog/index.html', context)