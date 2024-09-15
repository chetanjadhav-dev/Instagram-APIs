# views.py
from rest_framework import generics
from rest_framework.response import Response
from .models import InstagramPost
from .serializers import InstagramPostSerializer

class InstagramPostListView(generics.ListAPIView):
    serializer_class = InstagramPostSerializer

    def get_queryset(self):
        username = self.kwargs['username']
        start_id = self.kwargs['start_id']
        end_id = self.kwargs['end_id']
        return InstagramPost.objects.filter(
            profile__username=username,
            id__gte=start_id,
            id__lte=end_id
        )
