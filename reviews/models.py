from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from movies.models import Movie

class Review(models.Model):
    movie = models.ForeignKey(
        Movie, 
        on_delete=models.PROTECT, 
        related_name="reviews"
        )
    stars = models.IntegerField( # validators - tem funcoes prontas - pesquisas as funcoes do validators
        validators=[
            MinValueValidator(0, "avaliacao nao pode ser menor inferior a 0 estrelas."),
            MaxValueValidator(5, "avaliacao nao pode ser menor superior a 5 estrelas.")
        ]
    )
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.movie