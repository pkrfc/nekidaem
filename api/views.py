from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from posts.models import Follow, Post

from .serializers import FollowSerializer, PostSerializer, PostListSerializer


class PostViewSet(ModelViewSet):
    """Post create"""
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    ordering_fields = ('pub_date',)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class FollowViewSet(ModelViewSet):
    """Follow"""
    serializer_class = FollowSerializer

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_destroy(self, instance):
        instance.delete()


class PostsListViewSet(ReadOnlyModelViewSet):
    """Post list"""
    serializer_class = PostListSerializer()
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    ordering_fields = ('pub_date',)

    def get_queryset(self):
        followed_people = Follow.objects.filter(
            user=self.request.user).values('following'
                                           )
        return Post.objects.filter(author__in=followed_people)