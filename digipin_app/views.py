import requests
from django.http import JsonResponse
from django.shortcuts import render

def get_digipin(request):
    lat = request.GET.get("latitude")
    lon = request.GET.get("longitude")
    if not lat or not lon:
        return JsonResponse({"error": "Missing latitude or longitude"}, status=400)

    digipin = None
    try:
        url = f"http://localhost:5001/api/digipin/encode?latitude={lat}&longitude={lon}"
        res = requests.get(url)
        if res.ok:
            digipin = res.json().get("digipin")
            if digipin:
                return JsonResponse({"digipin": digipin})
            else:
                return JsonResponse({"error": "DigiPIN not found in API response"}, status=500)
        else:
            return JsonResponse({"error": "DigiPIN API returned an error"}, status=res.status_code)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

def home_view(request):
    return render(request, 'digipin_app/home.html')

def bookings_view(request):
    return render(request, 'digipin_app/bookings.html')