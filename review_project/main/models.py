from django.db import models

# Create your models here.

from django.db import models

class Review(models.Model):
    title = models.CharField(max_length=100, default="제목 없음")
    name = models.CharField(max_length=50)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title