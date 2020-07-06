from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from posts.serializers import PostDetailSerializer, PostsListSerializer
from posts.models import Post
from posts.permissions import IsOwnerOrReadOnly


class PostCreateView(generics.CreateAPIView):
    serializer_class = PostDetailSerializer
    permission_classes = (IsAuthenticated,)


class PostsListView(generics.ListAPIView):
    serializer_class = PostsListSerializer
    queryset = Post.objects.all()


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostDetailSerializer
    queryset = Post.objects.all()
    permission_classes = (IsOwnerOrReadOnly, IsAdminUser)
