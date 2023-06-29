from rest_framework.serializers import ModelSerializer
from .models import Board
from users.models import User
from users.serializers import UserSerializer
from reviews.serializers import ReviewSerializer

class BoardSerializer(ModelSerializer):
    users = UserSerializer()
    review_set = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Board
        fields ="__all__"
        # depth = 1

        