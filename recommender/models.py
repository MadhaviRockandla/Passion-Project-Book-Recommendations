from django.db import models

# Create your models here.
class recommender_book(models.Model):
    # name=models.CharField(max_length=200)
    UserID = models.CharField(max_length=200)
    BookTitle = models.CharField(max_length=200)
    BookRating = models.CharField(max_length=200)

    def __str__(self):
        return self.BookTitle