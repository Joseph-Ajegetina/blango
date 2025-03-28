from rest_framework import generics
from rest_framework.authentication import SessionAuthentication

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
    serializer_class = PostSerializer