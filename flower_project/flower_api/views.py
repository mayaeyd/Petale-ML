from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def predict_flower(request):
    if request.method == 'POST':
        return JsonResponse({'message':'Endpoint created'})
    return JsonResponse({'error': 'Only POST requests allowed'}, status=405)
