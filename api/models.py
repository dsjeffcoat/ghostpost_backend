from django.db import models
from django.utils import timezone

# Create your models here.


class GhostPost(models.Model):
    BOAST_OR_ROAST = (
        ('Boast', 'Boast'),
        ('Roast', 'Roast'),
    )

    is_boast = models.CharField(
        max_length=5, choices=BOAST_OR_ROAST)
    post = models.CharField(max_length=280, null=True, blank=True)
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)
    time_submitted = models.DateTimeField(default=timezone.now)
    sec_key = models.CharField(max_length=6)

    def __str__(self):
        return self.post

    def total_score(self):
        return self.upvote - self.downvote
