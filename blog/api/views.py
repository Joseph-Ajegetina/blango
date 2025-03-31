from rest_framework import generics
from rest_framework.authentication import SessionAuthentication

from blog.api.permissions import AuthorModifyOrReadOnly, IsAdminUserForObject

class PostList(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication]
from blog.api.serializers import PostSerializer
from blog.models import Post


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [SessionAuthentication]


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    permissions_classes = [AuthorModifyOrReadOnly | IsAdminUserForObject]
    serializer_class = PostSerializer