# urls.py
from django.urls import path
from .views import InstagramPostListView

urlpatterns = [
    path('<str:username>/<int:start_id>/<int:end_id>/', InstagramPostListView.as_view(), name='instagram-posts-range'),
]
