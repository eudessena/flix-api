import json
from django.http import JsonResponse
from genres.models import Genre
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404

# Create your views here.

@csrf_exempt
def genre_create_list_view(request):

    if request.method == 'GET':

        genres = Genre.objects.all()

        data = [{'id': genre.id, 'name': genre.name} for genre in genres]
    
        # OUUU

        # data = []

        # for genre in genres:
        #     data.append(
        #         {'id': genre.id, 'name': genre.name}
        #     )

        return JsonResponse(data, safe=False)

    elif request.method == 'POST':

        data = json.loads(request.body.decode('utf-8'))
        new_genre = Genre(name=data['name'])
        new_genre.save()
        return JsonResponse({'id': new_genre.id, 'name':  new_genre.name}, status=201)

@csrf_exempt
def genre_detail_view(request, pk):

    genre = get_object_or_404(Genre, pk=pk)

    if request.method == 'GET':
        data = {'id': genre.id, 'name': genre.name}
        return JsonResponse(data)
    
    elif request.method == 'PUT':
        # request.body é bytes b'{"name": "Rock"}' - Não é string ainda
        # .decode('utf-8') Converte bytes → string: '{"name": "Rock"}' 
        # json.loads() - Converte string JSON → objeto Python equivalente
        data = json.loads(request.body.decode('utf-8')) # recebi o objeto json
        genre.name = data['name'] # peguei o objeto com o genero carregado do banco e atualizei o campo name na variavel do objeto 
        genre.save() # salvei no banco o objeto atualizado
        return JsonResponse({'id': genre.id, 'name':  genre.name})
    
    elif request.method == 'DELETE':
        genre.delete()
        return JsonResponse({"message": "Deleted"}, status=204)
        