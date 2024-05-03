from django.shortcuts import render
import pickle
import os
from . import settings

model_path = os.path.join(settings.BASE_DIR, 'path', 'to', '../crop_recommendation_model.pkl')


def home(request):
    return render(request, "home.html")

def predict(request):
    return render(request, "predict.html")

def result(request):
    crop_dict = {
        'rice': 1,
        'maize': 2,
        'jute': 3,
        'cotton': 4,
        'coconut': 5,
        'papaya': 6,
        'orange': 7,
        'apple': 8,
        'muskmelon': 9,
        'watermelon': 10,
        'grapes': 11,
        'mango': 12,
        'banana': 13,
        'pomegranate': 14,
        'lentil': 15,
        'blackgram': 16,
        'mungbean': 17,
        'mothbeans': 18,
        'pigeonpeas': 19,
        'kidneybeans': 20,
        'chickpea': 21,
        'coffee': 22
    }
    # Load the pre-trained model
    with open('../crop_recommendation/crop_recommendation_model.pkl', 'rb') as f:
        model = pickle.load(f)

    print(type(model))


        # Extract user input from the GET request
    try:
        val1 = float(request.POST['nitrogen'])
        val2 = float(request.POST['phosphorus'])
        val3 = float(request.POST['potassium'])
        val4 = float(request.POST['temperature'])
        val5 = float(request.POST['humidity'])
        val6 = float(request.POST['ph'])
        val7 = float(request.POST['rainfall'])
    except (KeyError, ValueError):
        # Handle potential errors (missing keys or non-numeric values)
        return render(request, "predict.html", {"result2": "Erreur: Données insuffisantes ou incorrectes  pour predire la culture"})

        # Prepare the input data for prediction
    data = [[val1, val2, val3, val4, val5, val6, val7]]

    # Make prediction using the loaded model
    pred = model.predict(data)  # Assuming the model returns a single prediction

    # Look up the predicted crop using the crop dictionary
    predicted_crop_label = list(crop_dict.keys())[list(crop_dict.values()).index(int(pred))]

    # Prepare the recommendation result for the template
    result1 = f"Culture recommandée: {predicted_crop_label}"

    return render(request, "predict.html", {"result2": result1})