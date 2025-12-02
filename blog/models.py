from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
    
    def get_reading_time(self):
        """Calculate estimated reading time in minutes (assuming 200 words per minute)"""
        word_count = len(self.content.split())
        reading_time = max(1, round(word_count / 200))
        return reading_time