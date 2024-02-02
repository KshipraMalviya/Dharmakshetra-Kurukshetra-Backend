import json
from django.http import JsonResponse
from .main import get_recommendations, get_destinations
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def all_destinations_view(request):
    if request.method == 'GET':
        destinations = get_destinations()
        response_data = {
                'destinations': destinations.to_dict()
            }
        return JsonResponse(response_data)
    return JsonResponse({'error': 'Bad Request!'}, status=400)

@csrf_exempt
def recommendations_view(request):
    if request.method == 'POST':
        destination = json.loads(request.body).get('destination', '')
        if destination:
            recommendations = get_recommendations(destination)
            response_data = recommendations.to_dict(orient='records')
            return JsonResponse(response_data, safe=False)
        else:
            return JsonResponse({'error': 'Please enter some destination!'}, status=400)
