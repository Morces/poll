from django.http import HttpResponse
from django.shortcuts import redirect, render
from poll.forms import CreatePollForm, SignUpForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from poll.models import Poll, Profile

# Create your views here.
@login_required(login_url='login', redirect_field_name='index')
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
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form':form})

# def login(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         return redirect('index')
        
#     else:
#        return render(request, 'registration/login.html')

def logout(request):
    if request.method=="POST":
        logout(request)
        return redirect('login')

@login_required(login_url='login')
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

@login_required(login_url='login')
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

@login_required(login_url='login')
def results(request, poll_id):
    poll = Poll.objects.get(id=poll_id)
    params = {'poll':poll}
    return render(request, 'results.html',params)

@login_required(login_url='login')
def profile(request, pk):
    profile= Profile.objects.get(id=pk)
    context = {'profile':profile}  
    return render(request, 'profile.html', context)
