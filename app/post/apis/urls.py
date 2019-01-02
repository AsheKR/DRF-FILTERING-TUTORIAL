from django.urls import path

from post.apis.views import PostListCreateView

urlpatterns = [
    path('', PostListCreateView.as_view()),
]