from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    #path('contact/', views.contact, name='contact'),
    path('review/', views.review, name='review'),
    path('review/success/', views.review_success, name='review_success'),
    path('reviews/', views.review_list, name='review_list'),
    path('review/menu/', views.review_menu, name='review_menu'),
    path('review/<int:id>/edit/', views.edit_review, name='review_edit'),
    path('review/<int:id>/delete/', views.delete_review, name='review_delete'),
    path('contact/', views.contact, name='contact'),
    path('plist/', views.plist_home, name='plist_home'),
    path('plist/create/', views.plist_create, name='plist_create'),
    #로그인, 로그아웃
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    #회원가입
    path('signup/', views.signup, name='signup'),
    #p-list 내부
    path('plist/', views.plist_home, name='plist_home'),
    path('plist/<int:plist_id>/', views.plist_detail, name='plist_detail'),
    #리뷰 내부
    path('review/<int:review_id>/', views.review_detail, name='review_detail'),
    #p-list 삭제
    path('plist/<int:pk>/delete/', views.plist_delete, name='plist_delete'),

]