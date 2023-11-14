from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Comment
from .serializers import CommentSerializer

# Create your views here.


class CommentList(APIView):
    def get(self, request):
