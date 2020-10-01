from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import GhostPostSerializer
from .models import GhostPost

# Create your views here.


class GhostPostViewSet(viewsets.ModelViewSet):
    queryset = GhostPost.objects.all()
    serializer_class = GhostPostSerializer

    @action(detail=False)
    def boasts(self, request):
        boasts = GhostPost.objects.filter(
            is_boast=True).order_by('-time_submitted')
        serializer = self.get_serializer(boasts, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def roasts(self, request):
        roasts = GhostPost.objects.filter(
            is_boast=False).order_by('-time_submitted')
        serializer = self.get_serializer(roasts, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def highest_rated(self, request):
        posts = GhostPost.objects.all()
        votes = sorted(posts, key=lambda p: p.total_score(), reverse=True)

        serializer = self.get_serializer(votes, many=True)
        return Response(serializer.data)

    # TODO: HELP! This particular extra action is not working properly!

    # @action(detail=True, methods=['post'])
    # def upvote(self, request, pk=None):
    #     serializer = GhostPostSerializer(data=request.data)
    #     if serializer.is_valid():
    #         .upvote += 1
    #         post.save()
    #         return Response({'status': 'Vote is now entered'})
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)