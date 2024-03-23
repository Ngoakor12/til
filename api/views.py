from django.shortcuts import render
from django.http import Http404
from django.contrib.auth.models import Group, User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import Topic, Record
from .serializers import TopicSerializer, RecordSerializer

# Create your views here.


@api_view(["GET", "POST"])
def topic_list(request):
    """
    List all topics, or create a new topic.
    """

    if request.method == "GET":
        topics = Topic.objects.all()
        serializer = TopicSerializer(topics, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = TopicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def topic_detail(request, pk):
    """
    Retrieve, update or delete a topic.
    """

    try:
        topic = Topic.objects.get(pk=pk)
    except Topic.DoesNotExist:
        raise Http404

    if request.method == "GET":
        serializer = TopicSerializer(topic)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = TopicSerializer(topic, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        topic.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
