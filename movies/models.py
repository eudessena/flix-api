from django.db import models
from genres.models import Genre
from actors.models import Actor


class Movie(models.Model):
    title = models.CharField(max_length=200)  # ForeignKey ligacao um filme pode ter um genero, um genero pode ter muitos filmes
    genre = models.ForeignKey(
        Genre, 
        on_delete=models.PROTECT,
        related_name="movies"
    ) # related_name apelido da ligacao entre movies e genre
    release_date = models.DateField(null=True, blank=True)
    actors = models.ManyToManyField(
        Actor,
        related_name="movies"
    )  # ManyToManyField ligacao muito para muitos, ou seja um ator pra muitos filmes e um filme pode ter varios atores
    resume = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title