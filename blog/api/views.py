from rest_framework import generics
from rest_framework.authentication import SessionAuthentication

from blog.api.permissions import AuthorModifyOrReadOnly, IsAdminUserForObject

from blango_auth.models import User
from blog.api.serializers import PostSerializer, UserSerializer, PostDetailSerializer

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
    serializer_class = PostDetailSerializer

class UserDetail(generics.RetrieveAPIView):
    lookup_field = "email"
    queryset = User.objects.all()
    serializer_class = UserSerializer