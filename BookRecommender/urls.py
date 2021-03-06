"""BookRecommender URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('recommender/', include('recommender.urls'))
# ]

from accounts.views import (
    login_view,
    logout_view,
    register_view
)
from .views import HomePageView, SearchBooksView, AppBooksView
from .views import AboutPageView
urlpatterns = [
    path('', HomePageView.as_view(), name='home.html'),
    path('admin/', admin.site.urls),
    path('login/', login_view),
    path('logout/', logout_view),
    path('register/', register_view),
    path('recommender/', include('recommender.urls')),
    path('search_books/', SearchBooksView.as_view(), name='search_books.html'),
    path('app/', AppBooksView.as_view(), name='app.html'),
    path('about/', AboutPageView.as_view(), name='about'),
]