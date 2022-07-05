from django.db import models

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