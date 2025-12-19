from django.contrib import admin
from .models import PersonalList, PersonalListItem, Review

@admin.register(PersonalList)
class PersonalListAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'rating', 'author', 'created_at')

