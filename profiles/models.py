from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class Profile(models.Model):
    owner=models.OneToOneField(User, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    name=models.CharField(max_length=255, blank=True)
    content=models.TextField(blank=True)
    profile_image=models.FileField(upload_to='profile_images/', default='../kang1_ojzpwj', null=True, blank=True)
    video_file=models.FileField(upload_to='profile_videos/', null=True, blank=True)
    audio_file=models.FileField(upload_to='profile_audios/', null=True, blank=True)

    class Meta:
        ordering=['-created_at']

    def __str__(self):
        return f"{self.owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)

post_save.connect(create_profile, sender=User)


    


