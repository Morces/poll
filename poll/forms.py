from django.forms import ModelForm
from .models import Poll

class CreatePollForm(ModelForm):
    class Meta:
        model = Poll
        fields = ('question', 'choice1', 'choice2', 'choice3', 'choice4')