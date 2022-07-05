from django.http import HttpResponse
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
    poll = Poll.objects.get(id=poll_id)
    if request.method == "POST":
        choice_select = request.POST['poll']
        if choice_select == 'choice1':
            poll.choice1_count +=1
        elif choice_select == 'choice2':
            poll.choice2_cont +=1
        elif choice_select == 'choice3':
            poll.choice3_cont +=1
        elif choice_select == 'choice4':
            poll.choice4_cont +=1
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