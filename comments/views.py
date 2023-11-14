from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Comment
from .serializers import CommentSerializer

# Create your views here.


class CommentList(APIView):
    def get(self, request):
        comments = Comment.objects.filter(user=request.user.profile)
        data = CommentSerializer(comments, many=True).data
        return Response(data)

    def post(self, request):
        comment = Comment.objects.create(
            user=request.user.profile,
            post=request.data["post"],
            text=request.data["text"],
        )
        data = CommentSerializer(comment).data
        return Response(data)

    def put(self, request):
        comment = Comment.objects.get(id=request.data["id"])
        comment.text = request.data["text"]
        comment.save()
        data = CommentSerializer(comment).data
        return Response(data)

    def delete(self, request, pk):
        Comment.objects.get(id=pk).delete()
        return Response({"message": "با موفقیت پاک شد"})
