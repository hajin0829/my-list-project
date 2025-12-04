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
        category = request.POST.get("category")
        title = request.POST.get("title")
        content = request.POST.get("content")
        author = request.POST.get("author")

        Review.objects.create(
            category=category,
            title=title,
            content=content,
            author=author
        )


        return redirect('review_success')

    return render(request, 'main/review.html')


def review_success(request):
    return render(request, 'main/review_success.html')

def review_list(request):
    category = request.GET.get('category')

    if category:
        reviews = Review.objects.filter(category=category).order_by('-created_at')
    else:
        reviews = Review.objects.all().order_by('-created_at')

    return render(request, 'main/review_list.html', {
        'reviews': reviews,
        'selected_category': category
    })

def review_menu(request):
    return render(request, 'main/review_menu.html')

def edit_review(request, id):
    review = Review.objects.get(id=id)

    if request.method == "POST":
        review.category = request.POST.get("category")
        review.title = request.POST.get("title")
        review.author = request.POST.get("author")
        review.content = request.POST.get("content")
        review.save()

        return redirect('review_list')

    return render(request, 'main/edit_review.html', {'review': review})

def delete_review(request, id):
    review = Review.objects.get(id=id)
    review.delete()
    return redirect('review_list')
