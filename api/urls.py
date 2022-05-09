from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import FollowViewSet, PostsListViewSet, PostViewSet

router = DefaultRouter()


router.register('posts', PostViewSet, basename='posts')
router.register('follow', FollowViewSet, basename='follow')
router.register('posts-list', PostsListViewSet, basename='posts-list')

urlpatterns = [
    path('v1/', include(router.urls)),
    ]
