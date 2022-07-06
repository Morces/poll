from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class Poll(models.Model):
    question = models.TextField()
    choice1 = models.CharField(max_length=40, null=True)
    choice2 = models.CharField(max_length=40, null=True)
    choice3 = models.CharField(max_length=40, null=True)
    choice4 = models.CharField(max_length=40, null=True)
    choice1_count = models.IntegerField(default=0)
    choice2_count = models.IntegerField(default=0)
    choice3_count = models.IntegerField(default=0)
    choice4_count = models.IntegerField(default=0)

    def total(self):
        return self.choice1_count + self.choice2_count + self.choice3_count + self.choice4_count


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', null=True, blank=True)
    name = models.CharField(max_length=60, blank=True)
    phone = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=60)
    

    def __str__(self):
        return str(self.name)
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
