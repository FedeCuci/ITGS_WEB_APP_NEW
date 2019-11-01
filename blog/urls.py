from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    PostSortView,
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
    CommentDetailView,
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
    path('sorted/', PostSortView.as_view(), name='post-sorted'),
    path('post/<int:pk>/create/comment/', CommentCreateView.as_view(), name='comment-create'),
    path('post/<int:pk>/update/comment/<int:id>/', CommentUpdateView.as_view(), name='comment-update'),
    path('post/<int:pk>/delete/comment/<int:id>/', CommentDeleteView.as_view(), name='comment-delete'),
#    path('comment/<int:pk>/', CommentDetailView.as_view(), name='comment-detail')
]
