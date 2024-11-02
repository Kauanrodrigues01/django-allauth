from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')

@login_required(login_url='/')
def members(request):
    return render(request, 'members.html')