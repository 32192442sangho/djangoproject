from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from movies.movies.sevices import DcGan


@api_view(['GET'])
@parser_classes([JSONParser])
def face(request):
    DcGan().result()
    print(f'Enter Show Faces with {request}')
    return JsonResponse({'Response Test ': 'SUCCESS'})