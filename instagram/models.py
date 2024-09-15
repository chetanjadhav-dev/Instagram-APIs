from django.db import models

class InstagramProfile(models.Model):
    username = models.CharField(max_length=255, primary_key=True)
    post_count = models.IntegerField()

    def __str__(self):
        return self.username

class InstagramPost(models.Model):
    MEDIA_TYPE_CHOICES = [
        ('image', 'Image'),
        ('video', 'Video'),
        ('carousel', 'Carousel'),
    ]

    profile = models.ForeignKey(InstagramProfile, on_delete=models.CASCADE, related_name='posts', to_field='username')
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPE_CHOICES, default='image')
    image = models.CharField(max_length=100, blank=True, null=True)
    video = models.CharField(max_length=100, blank=True, null=True)
    caption = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.profile.username} - {self.caption[:30]}..."
