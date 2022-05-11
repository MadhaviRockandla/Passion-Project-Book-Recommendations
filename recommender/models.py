from django.db import models


# Create your models here.
def recommender_book():
    return models


class BRS_Dataset(models.Model):

    UserID = models.CharField(max_length=200)
    BookTitle = models.CharField(max_length=200)
    BookRating = models.CharField(max_length=200)

    def __str__(self):
        return self.BookTitle


