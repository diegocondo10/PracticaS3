from django.shortcuts import render
from django.http import JsonResponse
import requests
import base64
import json
from uuid import uuid4
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def subir_imagen(request):
    if request.method == 'POST':
        image = request.FILES['imagen']
        image_string = base64.b64encode(image.read()).decode('utf-8')
        extension = image.content_type.replace('image/', '.')
        response = requests.post(
            'https://n5w29niyjj.execute-api.us-east-1.amazonaws.com/testing',
            json=json.dumps({
                'body': image_string,
                'filename': f'{uuid4()}{extension}'
            })
        )
        return JsonResponse(response.json())
    return JsonResponse({
        'status': 400,
        'error': 'SOLO ENVIAR PETICION POR POST'
    })
