from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UploadedMedia

class FileUploadView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):
        file = request.FILES.get('file')
        if file:
            UploadedMedia.objects.create(file=file)
            return Response({"message": "File uploaded!"}, status=status.HTTP_201_CREATED)
        return Response({"error": "No file uploaded"}, status=status.HTTP_400_BAD_REQUEST)
