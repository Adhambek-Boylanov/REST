from django.db.models import Count
from rest_framework import status
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *

@api_view(["GET","POST"])
def actor_get_post(request):
    if request.method == "GET":
        posts = Actor.objects.all()
        serializer = ActorSerializers(posts,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    elif request.method =="POST":
        serializer = ActorSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
@api_view(["PUT","DELETE"])
def actor_put(requst,pk):
    if requst.method == "PUT":
        actor = get_object_or_404(Actor,pk = pk)
        serializer = ActorSerializers(actor,data=requst.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
    elif requst.method == "DELETE":
        actor = get_object_or_404(Actor,pk = pk)
        actor.delete()
        return Response(status=status.HTTP_200_OK)

class MovieApi(APIView):
    def post(self,request):
        serializer = MovieSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
    def get(self,request):
        movies = Movie.objects.all()
        serializer = MovieSerializers(movies, many = True)
        return Response(data=serializer.data,status=status.HTTP_201_CREATED)

class MovieDetailAPI(APIView):
    def get(self,request,pk):
        movie = get_object_or_404(Movie,pk = pk)
        serializer = MovieSerializers(movie)
        return Response(data=serializer.data,status=status.HTTP_201_CREATED)
    def put(self,request,pk):
        movies = get_object_or_404(Movie,pk = pk)
        serializer = MovieSerializers(movies,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
    def patch(self,request,pk):
        movies = get_object_or_404(Movie,pk = pk)
        serializer = MovieSerializers(movies,data=request.data,partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_200_OK)
    def delete(self,request,pk):
        movies = get_object_or_404(Movie,pk = pk)
        movies.delete()
        return Response(status=status.HTTP_200_OK)


class MovieDataAPI(APIView):
    def get(self, request, start_year = None, end_year=None):
        if end_year and end_year:
            movies = Movie.objects.filter(year__range=(start_year, end_year))
        elif start_year:
            movies = Movie.objects.filter(year=start_year)
        else:
            movies = Movie.objects.annotate(count_actor = Count('actor')).filter(count_actor__lt = 3).prefetch_related('actor')
        serializer = MovieSerializers(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)




