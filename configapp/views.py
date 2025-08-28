from http.client import responses

from django.db.models import Count
from rest_framework import status, generics, viewsets
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from drf_yasg.utils import swagger_auto_schema
from rest_framework.pagination import PageNumberPagination


class ActorApi(APIView):
    @swagger_auto_schema(request_body=ActorSerializers)
    def post(self, request):
        serializer = ActorSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request):
        actors = Actor.objects.all()
        serializer = ActorSerializers(actors, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(["PUT", "DELETE"])
def actor_put(requst, pk):
    if requst.method == "PUT":
        actor = get_object_or_404(Actor, pk=pk)
        serializer = ActorSerializers(actor, data=requst.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
    elif requst.method == "DELETE":
        actor = get_object_or_404(Actor, pk=pk)
        actor.delete()
        return Response(status=status.HTTP_200_OK)


class MovieApi(APIView):
    def post(self, request):
        serializer = MovieSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializers(movies, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class MovieDetailAPI(APIView):
    def get(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        serializer = MovieSerializers(movie)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, pk):
        movies = get_object_or_404(Movie, pk=pk)
        serializer = MovieSerializers(movies, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def patch(self, request, pk):
        movies = get_object_or_404(Movie, pk=pk)
        serializer = MovieSerializers(movies, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        movies = get_object_or_404(Movie, pk=pk)
        movies.delete()
        return Response(status=status.HTTP_200_OK)


class MovieDataAPI(APIView):
    def get(self, request, start_year=None, end_year=None):
        if end_year and end_year:
            movies = Movie.objects.filter(year__range=(start_year, end_year))
        elif start_year:
            movies = Movie.objects.filter(year=start_year)
        else:
            movies = Movie.objects.annotate(count_actor=Count('actor')).filter(count_actor__lt=3).prefetch_related(
                'actor')
        serializer = MovieSerializers(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CommitAPI(APIView):
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(request_body=CommitMovieSerializers)
    def post(self, request):
        response = {"success":True}
        serializer = CommitMovieSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(author = request.user)
            response["data"] = serializer.data
            return Response(data=response)
        return Response(data=serializer.data)

    def get(self, request):
        response = {'success':True}
        commit = CommitMovie.objects.filter(author= request.user)
        serializer = CommitMovieSerializers(commit, many=True)
        response["data"] = serializer.data
        return Response(data=response)

    def put(self, request, pk):
        commit = get_object_or_404(CommitMovie, pk=pk)
        serializer = MovieSerializers(commit, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, pk):
        commit = get_object_or_404(CommitMovie, pk=pk)
        commit.delete()
        return Response(status=status.HTTP_200_OK)


# class ProductApi(generics.ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerialixers
#
#
# class CustomPagination(PageNumberPagination):
#     page_size = 1
#
#
# class SaleListCreate(generics.ListCreateAPIView):
#     queryset = Sale.objects.all()
#     serializer_class = SaleSerializers

    # pagination_class = CustomPagination
