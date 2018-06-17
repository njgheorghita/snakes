from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Repo


def index(request):
    template = loader.get_template('snakes/index.html')
    context = {
        'eth_repos': Repo.objects.all(),
        'pr_images': Repo.five_images(),
    }
    return HttpResponse(template.render(context, request))
