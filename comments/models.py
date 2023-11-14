from django.db import models
from users.models import Profile
from posts.models import Post

# Create your models here.


class Comment(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "نظرات"

    def __str__(self) -> str:
        return f"{self.text[:50]}......"
