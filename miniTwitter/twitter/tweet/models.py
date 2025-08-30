from django.db import models
from django.contrib.auth.models import User


class Tweet(models.Model):   # Class names in PascalCase (best practice)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=240)  # CharField for 240 chars
    photo = models.ImageField(upload_to='photos', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.text[:10]}"