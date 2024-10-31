from django.db import models
from django.contrib.auth.models import User
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    font_style = models.CharField(max_length=50, default='Arial')  # Default font

    def __str__(self):
        return self.user.username