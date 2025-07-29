import requests
from django.http import JsonResponse

def get_digipin(request):
    lat = request.GET.get("lat")
    lon = request.GET.get("lon")

    if not lat or not lon:
        return JsonResponse({"error": "Missing lat/lon"}, status=400)

    try:
        url = f"http://localhost:5001/api/digipin/encode?latitude={lat}&longitude={lon}"
        response = requests.get(url)

        # Check if the response is valid JSON
        return JsonResponse(response.json(), safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
