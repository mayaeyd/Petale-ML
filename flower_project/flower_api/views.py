from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import tensorflow as tf
import json
from PIL import Image
import io
import numpy as np

# Load model and labels
model = tf.keras.models.load_model('flower_model.h5')
with open('class_labels.json', 'r') as f:
    class_labels = json.load(f)

@csrf_exempt
def predict_flower(request):
    if request.method == 'POST':
         try:
            # Get image from request
            image_file = request.FILES['image']
            image = Image.open(io.BytesIO(image_file.read()))
            
            # Preprocess image
            image = image.resize((64, 64))
            image_array = tf.keras.preprocessing.image.img_to_array(image)
            image_array = np.expand_dims(image_array, axis=0)
            image_array = image_array / 255.0

        return JsonResponse({'message':'Endpoint created'})
    return JsonResponse({'error': 'Only POST requests allowed'}, status=405)
