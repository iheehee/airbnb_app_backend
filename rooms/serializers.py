from rooms.models import Room
from users.serializers import RelatedUserSerializer
from rest_framework import serializers


class RoomSerializer(serializers.ModelSerializer):

    user = RelatedUserSerializer()

    class Meta:
        model = Room
        exclude = ("modified",)
        read_only_fields = ("user", "id", "created", "updated")

    def validate_beds(self, beds):
        if beds < 5:
            raise serializers.ValidationError("Your house is too small")
        else:
            return beds

    def validate(self, data):
        if not self.instance:
            check_in = data.get("check_in")
            check_out = data.get("check_out")
            if check_in == check_out:
                raise serializers.ValidationError("Not enough time between changes")
        return data


class BigRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        exclude = ()
