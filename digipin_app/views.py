import requests
from django.http import JsonResponse
from django.shortcuts import render


# def get_digipin(request):
#     lat = request.GET.get("lat")
#     lon = request.GET.get("lon")

#     if not lat or not lon:
#         return JsonResponse({"error": "Missing lat/lon"}, status=400)

#     try:
#         url = f"http://localhost:5001/api/digipin/encode?latitude={lat}&longitude={lon}"
#         response = requests.get(url)

#         # Check if the response is valid JSON
#         return JsonResponse(response.json(), safe=False)
#     except Exception as e:
#         return JsonResponse({"error": str(e)}, status=500)

# digipin_app/views.py
from django.shortcuts import render
import requests

def get_digipin(request):
    lat = request.GET.get("lat")
    lon = request.GET.get("lon")
    digipin = None
    error = None

    if lat and lon:
        try:
            url = f"http://localhost:5001/api/digipin/encode?latitude={lat}&longitude={lon}"
            res = requests.get(url)
            if res.ok:
                digipin = res.json().get("digipin")
            else:
                error = "DigiPIN API returned an error"
        except Exception as e:
            error = str(e)

    return render(request, "digipin_app/home.html", {
        "digipin": digipin,
        "error": error
    })
