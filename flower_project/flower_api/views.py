from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import tensorflow as tf
import json

# Load model and labels
model = tf.keras.models.load_model('flower_model.h5')
with open('class_labels.json', 'r') as f:
    class_labels = json.load(f)

@csrf_exempt
def predict_flower(request):
    if request.method == 'POST':
        return JsonResponse({'message':'Endpoint created'})
    return JsonResponse({'error': 'Only POST requests allowed'}, status=405)
