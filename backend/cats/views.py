from rest_framework.decorators import api_view
from rest_framework.response import Response
import base64
from .models import CatImage



@api_view(['GET'])
def show_cat(request, pk):
    cat = CatImage.objects.get(pk=pk)  # Fetch Cat Image by primary key
    image_base64 = base64.b64encode(cat.image).decode('utf-8')  # Convert binary to base64 photo
    return Response({'id': cat.id, 'description': cat.description, 'image_base64': image_base64})

