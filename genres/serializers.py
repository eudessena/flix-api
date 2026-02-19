from rest_framework import serializers
from genres.models import Genre


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre # setando o model
        fields = "__all__" # todos os campos para serem serializados, variacoes  fields = ["name", etc] passando campo a campo a ser serializado e retornado