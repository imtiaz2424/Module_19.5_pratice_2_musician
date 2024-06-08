from django.db import models
from musicians.models import Musician

# Create your models here.
class Album(models.Model):
    album_name = models.CharField(max_length=200)    
    release_date = models.DateTimeField(auto_now_add=True)
    RATING_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    rating = models.IntegerField(choices=RATING_CHOICES)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    # album = models.ManyToManyField(Musician, on_delete=models.CASCADE)

    def __str__(self):
        return self.album_name