from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import User
from .serializers import UserSerializer

# GET: 전체 리뷰 데이터 가져오기
class Users(APIView):
    def get(self, request):
        users = User.objects.all()  # 장고 객체

        # serializer(장고 객체 -> JSON)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


# get: 특정 리뷰 데이터 가져오기
class UserDetail(APIView):
    def get(self, request, user_id):
        try:
            user = User.objects.get(id = user_id)
        except User.DoesNotExist:
            raise NotFound

        serializer = UserSerializer(user)
        return Response(serializer.data)