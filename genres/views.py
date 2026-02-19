from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from genres.models import Genre
from genres.serializers import GenreSerializer

# Create your views here.

# a view generica espera um model e um serializer

class GenreCreateListView(ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class GenreRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
        