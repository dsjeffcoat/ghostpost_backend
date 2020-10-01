from .models import GhostPost
from rest_framework import serializers


class GhostPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = GhostPost
        fields = ['is_boast', 'post', 'total_score',
                  'upvote', 'downvote', 'time_submitted']