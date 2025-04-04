from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response 
from rest_framework.authentication import SessionAuthentication

from blog.api.permissions import AuthorModifyOrReadOnly, IsAdminUserForObject

from blango_auth.models import User
from blog.api.serializers import PostSerializer, UserSerializer, PostDetailSerializer, TagSerializer
from blog.models import Post, Tag

class PostList(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication]



class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [SessionAuthentication]


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    permissions_classes = [AuthorModifyOrReadOnly | IsAdminUserForObject]
    serializer_class = PostDetailSerializer

class PostViewSet(viewsets.ModelViewSet):
  permissions_classes = [AuthorModifyOrReadOnly | IsAdminUserForObject]
  queryset = Post.objects.all()

  def get_serializer_class(self):
    if self.action in ("list", "create"):
      return PostSerializer
    return PostDetailSerializer

class UserDetail(generics.RetrieveAPIView):
    lookup_field = "email"
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TagViewSet(viewsets.ModelViewSet):
  queryset = Tag.objects.all()
  serializer_class = TagSerializer

  @action(methods=["get"], detail=True, name="Posts with the Tag")
  def posts(self, request, pk=None):
    tag = self.get_object()
    post_serializer = PostSerializer(tag.posts, many=True, context={"request": request})
    return Response(post_serializer.data)