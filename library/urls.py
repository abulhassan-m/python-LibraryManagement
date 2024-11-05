# library/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),  # Landing page
    path('books/', views.book_list, name='book_list'),
    path('books/add/', views.add_book, name='add_book'),
    path('books/update/<int:pk>/', views.update_book, name='update_book'),
    path('books/delete/<int:pk>/', views.delete_book, name='delete_book'),
    path('members/', views.member_list, name='member_list'),
    path('members/add/', views.add_member, name='add_member'),
    path('members/update/<int:pk>/', views.update_member, name='update_member'),
    path('members/delete/<int:pk>/', views.delete_member, name='delete_member'),
    path('borrow/', views.borrow_book, name='borrow_book'),
    path('borrowed/', views.borrowed_books, name='borrowed_books'),
    path('return/<int:pk>/', views.return_book, name='return_book'),
    path('register/', views.register, name='register'),
    #path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'), 
    path('login/', views.user_login, name='login'),   
    path('logout/', views.user_logout, name='logout'),
    # path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('dashboard/', views.dashboard, name='user_dashboard'),
    path('report/', views.report, name='report'),
]
