from django.shortcuts import redirect, render
from poll.forms import CreatePollForm

from poll.models import Poll

# Create your views here.
def index(request):
    polls = Poll.objects.all()
    params = {'polls':polls}
    return render(request, 'index.html', params)

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
    params = {}
    return render(request, 'vote.html',params)

def results(request, poll_id):
    params = {}
    return render(request, 'results.html',params)