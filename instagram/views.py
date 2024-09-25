# views.py
from rest_framework import generics
from rest_framework.response import Response
from .models import InstagramPost
from .serializers import InstagramPostSerializer

class InstagramPostListView(generics.ListAPIView):
    serializer_class = InstagramPostSerializer

    def get_queryset(self):
        username = self.kwargs['username']
        start_id = int(self.kwargs['start_id']) - 1  # Starting index
        end_id = int(self.kwargs['end_id'])    # Number of posts to retrieve

        # Filter posts by username and order them by 'id'
        posts = InstagramPost.objects.filter(
            profile__username=username
        ).order_by('id')  # Assuming you want to order by the post ID or timestamp
        
        # Slice the queryset to start from the start_id and retrieve end_id posts
        return posts[start_id:start_id + end_id]

