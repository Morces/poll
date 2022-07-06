from django import forms
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Poll

class CreatePollForm(ModelForm):
    class Meta:
        model = Poll
        fields = ('question', 'choice1', 'choice2', 'choice3', 'choice4')

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=100, help_text='Type a valid email address!')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
