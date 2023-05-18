from django.urls import path, include
from rest_framework import routers

from .views import PostListAPIView, UserPostAPIView, UpvoteAPIView

router = routers.SimpleRouter()
router.register('upvote', UpvoteAPIView)
router.register('post', PostListAPIView)


urlpatterns = [
    path('up/', include(router.urls)),
    path('<username>/', UserPostAPIView.as_view()),
]
