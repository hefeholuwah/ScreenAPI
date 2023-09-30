from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import ScreenRecording
from .serializers import ScreenRecordingSerializer  # You'll need to create this serializer

@api_view(['POST'])
def create_screen_recording(request):
    serializer = ScreenRecordingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
