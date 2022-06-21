from rooms.models import Room
from users.serializers import TinyUserSerializer
from rest_framework import serializers


class RoomSerializer(serializers.ModelSerializer):

    user = TinyUserSerializer()

    class Meta:
        model = Room
        fields = ("name", "price", "bedrooms", "instant_book", "user")
