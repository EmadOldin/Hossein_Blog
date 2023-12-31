from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer

# Create your views here.


class PostList(APIView):
    def get(self, request):
        posts = Post.objects.filter(user=request.user.profile)
        data = PostSerializer(posts, many=True).data
        return Response(data)

    def post(self, request):
        post = Post.objects.create(
            title=request.data["title"],
            user=request.user.profile,
            text=request.data["text"],
        )
        data = PostSerializer(post).data
        return Response(data)

    def put(self, request):
        post = Post.objects.get(id=request.data["id"], user=request.user.profile)
        post.title = request.data["title"]
        post.text = request.data["text"]
        post.save()
        data = PostSerializer(post).data
        return Response(data)

    def delete(self, request, pk):
        Post.objects.get(id=pk, user=request.user.profile).delete()
        return Response({"message": "با موفقیت پاک شد"})
