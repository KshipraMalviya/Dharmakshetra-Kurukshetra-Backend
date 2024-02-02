from django.urls import path
from .views import recommendations_view, all_destinations_view

urlpatterns = [
    path('', all_destinations_view),
    path('recommendations/', recommendations_view),
]
