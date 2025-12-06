from django.shortcuts import render, redirect
from .forms import PersonalListForm
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

def contact(request):
    return render(request, 'main/contact.html')

from .models import Review, PersonalList, PersonalListItem

def plist_home(request):
    lists = PersonalList.objects.all().order_by('-created_at')
    return render(request, 'main/plist_home.html', {'lists': lists})

def plist_create(request):
    reviews = Review.objects.all().order_by('-created_at')

    if request.method == 'POST':
        list_name = request.POST.get('name')
        selected_reviews = request.POST.getlist('reviews')

        # 리스트 생성
        plist = PersonalList.objects.create(name=list_name, cover_image=request.FILES.get("cover_image"))
        

        # 선택된 리뷰를 리스트에 추가
        for r_id in selected_reviews:
            PersonalListItem.objects.create(
                personal_list=plist,
                review_id=r_id
            )

        return redirect('plist_home')
    
    if request.method == "POST":
        form = PersonalListForm(request.POST, request.FILES)

        if form.is_valid():
            plist = form.save()
            
            # 선택된 리뷰 처리
            selected_reviews = request.POST.getlist("selected_reviews")
            plist.reviews.set(selected_reviews)

            return redirect("plist_list")
        
    else:
        form = PersonalListForm()

    return render(request, "main/plist_create.html", {
        "form": form,
        "reviews": reviews
    })
    
    