from django.shortcuts import render

from .models import Theme


def index(request):
    themes_list = Theme.objects.all()
    context = {'themes_list': themes_list}
    return render(request, 'blog/index.html', context)