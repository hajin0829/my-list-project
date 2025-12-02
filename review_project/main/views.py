from django.shortcuts import render, redirect
from .models import Review
from django.http import HttpResponse

# Create your views here.

def home(request):
    context = {'greeting': '안녕하세요'}
    return render(request, 'main/home.html', context)

def about(request):
    return render(request, 'main/about.html')

def add_review(request):
    return render(request, 'main/add_review.html')

def review(request):
    if request.method == "POST":
        Review.objects.create(
            title=request.POST['title'],
            name=request.POST['name'],
            message=request.POST['message']
        )

        return redirect('review_success')

    return render(request, 'main/review.html')


def review_success(request):
    return render(request, 'main/review_success.html')