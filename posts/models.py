from django.db import models
from users.models import Profile

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name_plural = "پست ها"

    def __str__(self) -> str:
        return f"{self.title} ---> {self.user}"
