from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def create(request):
    params = {}
    return render(request, 'create.html', params)

def vote(request, poll_id):
    params = {}
    return render(request, 'vote.html',params)

def results(request, poll_id):
    params = {}
    return render(request, 'results.html',params)