from django.urls import path
from . import views

urlpatterns = [
    path('api/screen-recordings/', views.create_screen_recording, name='create_screen_recording'),
    # Add more URL patterns as needed for your application
]
