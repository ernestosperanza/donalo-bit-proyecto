from django.urls import path, re_path
from .views import (PostListView,
                    PostDetailView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView,
                    UserPostListView,
                    DonarView)
from . import views

urlpatterns = [
    path('', views.about, name='blog-home'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-post'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/donar/<int:pk>/', DonarView.as_view(), name='post-donar'),
    path('about/', views.about, name='blog-about'),
    re_path(r'^list', views.post_list, name='blog-filter'),
]
