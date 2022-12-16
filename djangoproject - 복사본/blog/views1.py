from django.http import JsonResponse

from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser


@api_view(['POST'])
@parser_classes([JSONParser])
def stroke(request):
    print(f'Enter Stroke with {request}')
    return JsonResponse({'Response Test ': 'SUCCESS'})
