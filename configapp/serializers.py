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

# class SaleSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Sale
#         fields = "__all__"
#
# class ProductSerialixers(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = "__all__"