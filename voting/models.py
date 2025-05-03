from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Entry(models.Model):
    text = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:50]
    
    @property
    def vote_count(self):
        return self.votes.count()
    
class Vote(models.Model):
    entry = models.ForeignKey(Entry, related_name='votes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    session_id = models.CharField(max_length=100)

    class Meta:
        # Prevent duplicate votes from the same session????
        #unique_together = ('entry', 'session_id')
        pass