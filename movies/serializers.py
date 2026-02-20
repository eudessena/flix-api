from rest_framework.serializers import ModelSerializer

from movies.models import Movie

class MovieSerializer(ModelSerializer):
    class meta:
        model = Movie
        fields = "__all__"