from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import GhostPostSerializer
from .models import GhostPost
import string
import random
from django.http import JsonResponse
from django.middleware.csrf import get_token

# Create your views here.


def csrf(request):
    return JsonResponse({'csrfToken': get_token(request)})


def ping(request):
    return JsonResponse({'result': 'OK'})


class GhostPostViewSet(viewsets.ModelViewSet):
    queryset = GhostPost.objects.all().order_by('-time_submitted')
    serializer_class = GhostPostSerializer

    @action(detail=False)
    def boasts(self, request):
        boasts = GhostPost.objects.filter(
            is_boast='Boast').order_by('-time_submitted')
        serializer = self.get_serializer(boasts, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def roasts(self, request):
        roasts = GhostPost.objects.filter(
            is_boast='Roast').order_by('-time_submitted')
        serializer = self.get_serializer(roasts, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def highest_rated(self, request):
        posts = GhostPost.objects.all()
        votes = sorted(posts, key=lambda p: p.total_score(), reverse=True)

        serializer = self.get_serializer(votes, many=True)
        return Response(serializer.data)

    # TODO: HELP! This particular extra action is not working properly!

    @action(detail=True, methods=['post', 'get'])
    def upvote(self, request, pk=None):
        post = self.get_object()
        serializer = GhostPostSerializer(data=request.data)
        if serializer.is_valid():
            post.upvote += 1
            post.save()
            return Response({'status': 'Vote is now entered'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post', 'get'])
    def downvote(self, request, pk=None):
        post = self.get_object()
        serializer = GhostPostSerializer(data=request.data)
        if serializer.is_valid():
            post.downvote += 1
            post.save()
            return Response({'status': 'Vote is now entered'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
