from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from post.apis.filters import PostFilter
from post.apis.serailizers import PostSerializer
from post.models import Post


class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = (DjangoFilterBackend, )
    filter_class = PostFilter
