import json

from django.http import JsonResponse, QueryDict
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
import tensorflow as tf

from dlearn.fashion_service import FashionService

@api_view(['POST', 'GET'])
def find_fashion(request):
    if request.method == 'POST':
        print('POST')
        body = request.body
        print(f"### request.body is {body} ###")
        data = json.loads(body)
        print(request.headers)
        print(request.content_type)
        print(f"### REACT ID IS {data} ###")
        result = FashionService().service_model(data)
        return JsonResponse({'result': result})
    elif request.method == 'GET':
        print('GET')
        print(f"### REACT ID IS {request.GET['testNum']} ###")
        result = FashionService().service_model(int(request.GET['testNum']))
        return JsonResponse({'result': result})

def find_error(request,testNum):
    print(f"aaaaaaaaaaaaaaaaaaaaaaaa{request}")
    print(f"bbbbbbbbbbbbbbbbbbbbbbbb{testNum}")