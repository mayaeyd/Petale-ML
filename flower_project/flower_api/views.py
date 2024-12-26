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

            # Make prediction
            prediction = model.predict(image_array)
            predicted_class = np.argmax(prediction[0])
            confidence = float(prediction[0][predicted_class])
            flower_name = class_labels[str(predicted_class)]
            
            # Save prediction
            flower_pred = FlowerPrediction(
                image=image_file,
                prediction=flower_name,
                confidence=confidence
            )
            flower_pred.save()
            
            return JsonResponse({
                'flower': flower_name,
                'confidence': confidence
            })


        return JsonResponse({'message':'Endpoint created'})
    return JsonResponse({'error': 'Only POST requests allowed'}, status=405)
