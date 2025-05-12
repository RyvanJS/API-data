from django.urls import path
from .views import (
    BlogPostList, BlogPostDetail,
    UserList, UserDetail, RegisterView, 
    LoginView, TokenLoginView
)

urlpatterns = [
    path('posts/', BlogPostList.as_view(), name='post-list'),
    path('posts/<int:pk>/', BlogPostDetail.as_view(), name='post-detail'),
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('token-login/', TokenLoginView.as_view(), name='token-login'),
]
