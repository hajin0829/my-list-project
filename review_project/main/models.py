from django.db import models

# Create your models here.

from django.db import models

class Review(models.Model):
    CATEGORY_CHOICES = [
        ('movie', '영화'),
        ('book', '도서'),
        ('music', '노래'),
    ]

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=50)

    def __str__(self):
        return f"[{self.get_category_display()}] {self.title}"