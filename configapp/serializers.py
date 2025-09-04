from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import *
class ActorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = "__all__"

class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"


class CommitMovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = CommitMovie
        fields = ['id','title','author','movie']
        read_only_fields = ["author"]
class LoginSerializers(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self,attrs):
        username = attrs.get("username")
        password = attrs.get("password")

        try:
            user = User.objects.get(username = username)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                {
                    "success":False,
                    "detail":"User does not exist"
                }
            )
        auth_user = authenticate(username = user.username,password = password)
        if auth_user is None:
            raise serializers.ValidationError(
                {
                    "success":False,
                    "detail":"Username or password is invalid"
                }
            )
        attrs["user"] = auth_user
        return attrs
# class SaleSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Sale
#         fields = "__all__"
#
# class ProductSerialixers(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = "__all__"