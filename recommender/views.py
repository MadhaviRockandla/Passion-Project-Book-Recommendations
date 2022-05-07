# from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.


# def say_hello(request):
#     return HttpResponse('Hi! Welcome to books world')
#     ##return render(request, 'hello.html', {'name': 'Madhavi'})


from django.shortcuts import render
from django.http import HttpResponse
import requests

from django.views.generic import TemplateView
from .models import recommender_book

from .engine import runEngine
from .coldengine import coldrunEngine

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

# class AppPageView(TemplateView):
#     template_name = 'app.html'

# placeholder
def index(request):
    return HttpResponse('Hi! Welcome to books world')

def search_books(request):
    if request.method == "POST":
        search_ui = request.POST['searched']
        search_ui = int(search_ui)
        runEngine(search_ui)
        books = recommender_book.objects.filter(UserID=search_ui)
        return render(request, 'search_books.html',
                        {'searched': search_ui,
                         'books': books})
    else:
        return render(request, 'search_books.html', {})



def app(request):
    if request.method == "POST":
        horror = request.POST['horror']
        romance = request.POST['romance']
        thriller = request.POST['thriller']
        nonfiction = request.POST['nonfiction']
        coldrunEngine(horror, romance, thriller, nonfiction)
        books = recommender_book.objects.filter(UserID=1)
        return render(request, 'app.html',
                        {'searched': f"Horror: {horror}\n "
                                     f"Romance: {romance}\n "
                                     f"Thriller: {thriller}\n "
                                     f"Non-Fiction: {nonfiction}\n ",
                         'books': books})
    else:
        return render(request, 'app.html', {})
