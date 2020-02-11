from django.http import JsonResponse
import requests
import base64
import json
from uuid import uuid4
from django.views.decorators.csrf import csrf_exempt

URL = 'https://rnkpgpxpa1.execute-api.us-east-1.amazonaws.com'


# Create your views here.
@csrf_exempt
def subir_imagen(request):
    if request.method == 'POST':
        image = request.FILES['imagen']
        image_string = base64.b64encode(image.read()).decode('utf-8')
        extension = image.content_type.replace('image/', '.')
        response = requests.post(
            f'{URL}/prueba/subir-imagen',
            json=json.dumps({
                'imagen': image_string,
                'nombre': f'{uuid4()}{extension}'
            })
        )
        return JsonResponse(response.json())
    return JsonResponse({
        'status': 400,
        'error': 'SOLO ENVIAR PETICION POR POST'
    })


@csrf_exempt
def subir_imagen_s3(request):
    if request.method == 'POST':
        print('REQUEST:')
        data = json.loads(request.body)
        response = requests.post(
            f'{URL}/prueba/subir-imagen',
            json=json.dumps(
                json.loads(request.body)
            )
        )
        return JsonResponse(response.json())
    return JsonResponse({
        'status': 400,
        'error': 'SOLO ENVIAR PETICION POR POST'
    })
