from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from .serializers import UserSerializer
from django.contrib.auth.models import User

# from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.


class UserList(APIView):
    def get(self, request):
        users = Profile.objects.all()
        data = UserSerializer(users, many=True).data
        return Response(data)

    def post(self, request):
        first_name = request.data["first_name"]
        last_name = request.data["last_name"]
        email = request.data["email"]
        password = request.data["password"]

        user = User.objects.create_user(
            username=email,
            password=password,
            is_staff=False,
            is_superuser=False,
        )
        data = UserSerializer(user).data
        return Response(data)

    def put(self, request):
        first_name = request.data["first_name"]
        last_name = request.data["last_name"]
        email = request.data["email"]
        password = request.data["password"]

        user = User.objects.create_user(
            username=email,
            password=password,
            is_staff=False,
            is_superuser=False,
        )
        data = UserSerializer(user).data
        return Response(data)

    def delete(self, request, pk):
        Profile.objects.get(id=pk).delete()
        return Response({"message": "با موفقیت حذف شد"})
