from django.db import models

# Create your models here.

from django.db import models
from django.conf import settings

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
    
    # 개인 리스트 (리스트 제목만 가진 상위 객체)
class PersonalList(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null = True, blank = True)
    title = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to='plist_covers/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    reviews = models.ManyToManyField(Review, through="PersonalListItem")

    def __str__(self):
        return self.name


# 리스트에 담긴 항목 (리뷰에서 선택)
class PersonalListItem(models.Model):
    personal_list = models.ForeignKey(PersonalList, on_delete=models.CASCADE, related_name='items')
    review = models.ForeignKey(Review, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.personal_list.name} - {self.review.title}"
