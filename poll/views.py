from django.http import HttpResponse
from django.shortcuts import redirect, render
from poll.forms import CreatePollForm, SignUpForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from poll.models import Poll, Profile

# Create your views here.
@login_required(login_url='login')
def index(request):
    polls = Poll.objects.all()
    params = {'polls':polls}
    return render(request, 'index.html', params)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=password)
            login(request,user)
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form':form})


def logout(request):
    logout(request)
    return redirect('login' )

def create(request):
    if request.method == 'POST':
        form = CreatePollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreatePollForm()
    params = {'form':form}
    return render(request, 'create.html', params)

def vote(request, poll_id):
    poll = Poll.objects.get(id=poll_id)
    if request.method == "POST":
        choice_select = request.POST['poll']
        if choice_select == 'choice1':
            poll.choice1_count +=1
        elif choice_select == 'choice2':
            poll.choice2_count +=1
        elif choice_select == 'choice3':
            poll.choice3_count +=1
        elif choice_select == 'choice4':
            poll.choice4_count +=1
        else:
            return HttpResponse(400, 'Invalid!')
        poll.save()
        return redirect('results', poll.id)
    params = {'poll':poll}
    return render(request, 'vote.html',params)

def results(request, poll_id):
    poll = Poll.objects.get(id=poll_id)
    params = {'poll':poll}
    return render(request, 'results.html',params)

def profile(request, pk):
    profile= Profile.objects.get(id=pk)
    context = {'profile':profile}  
    return render(request, 'profile.html', context)
