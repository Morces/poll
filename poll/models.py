from django.db import models

# Create your models here.
class Poll(models.Model):
    question = models.TextField()
    choice1 = models.CharField(max_length=40)
    choice2 = models.CharField(max_length=40)
    choice3 = models.CharField(max_length=40)
    choice1_count = models.IntegerField(default=0)
    choice2_count = models.IntegerField(default=0)
    choice3_count = models.IntegerField(default=0)