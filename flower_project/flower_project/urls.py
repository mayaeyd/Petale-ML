from django.urls import path, include

urlpatterns = [
    path('', include('flower_api.urls')),
]