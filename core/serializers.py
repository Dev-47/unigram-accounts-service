from rest_framework import serializers

from core.models import User


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True, required=True, style={"input_type": "password"}
    )

    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "username",
            "password",
            "usertype",
            "created_at",
            "updated_at",
        ]
        extra_kwargs = {"password": {"write_only": True}}
        read_only_fields = ["usertype"]

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()

        return user
