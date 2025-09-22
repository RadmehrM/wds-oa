from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Contact
from .serializers import ContactSerializer



@api_view(['POST'])
def save_contact(request):
    serializer = ContactSerializer(data=request.data)  # Deserialize incoming data
    if serializer.is_valid():
        serializer.save()  # Save to database
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
