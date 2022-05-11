from django.contrib import admin
from recommender.models import recommender_book



class recommender_bookAdmin(admin.ModelAdmin):

    admin.site.register(recommender_book, admin)
# Register your models here.
