from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from .forms import CandidateForm

# Create your views here.

def home(request):
    return render(request, 'accounts/home.html')

def signup_view(request):
    if request.method == 'POST':
        form = CandidateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registered Successfully')
            return HttpResponseRedirect('/')
    else:
        form = CandidateForm()
    return render(request, 'accounts/signup.html', {'form':form})

