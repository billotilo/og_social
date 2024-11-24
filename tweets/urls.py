from django.urls import include, path

from . import views


urlpatterns = [
    path('', views.PostListView.as_view(), name="homefeeds"),
    path('post/<int:pk>', views.PostDetailView.as_view(), name="post-detail"),
    path('account/<int:pk>', views.UserAccountPostListView.as_view(), name="post-list-by-user"),

    path('post/create/', views.PostTweetCreate.as_view(), name='post-create'),
    path('comment/<int:pk>/create/', views.PostCommentCreate.as_view(), name='comment-create'),
]

