from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories

def index(request):

    categories = Categories.objects.all()

    context = {
        'title' : 'LoverLace - Главная',
        'content' : "Магазин нижнего белья LoverLace",
        'categories': categories
    }

    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'LoverLace - О нас',
        'content': "О нас",
        'text_on_page' : "Текст о том почему этот магазин такой классный и какой хороший товар."
    }

    return render(request, 'main/about.html', context)

