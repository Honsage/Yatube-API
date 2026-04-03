from django.urls import include, path

from rest_framework import routers
from rest_framework.authtoken import views

from .views import GroupViewSet, PostViewSet, CommentViewSet


router = routers.DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('groups', GroupViewSet, basename='groups')

urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('v1/', include(router.urls)),
    path('v1/posts/<int:post_id>/comments/',
         CommentViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('v1/posts/<int:post_id>/comments/<int:pk>/',
         CommentViewSet.as_view({'get': 'retrieve',
                                 'put': 'update',
                                 'patch': 'partial_update',
                                 'delete': 'destroy'})),
]
