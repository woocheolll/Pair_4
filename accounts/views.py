from django.shortcuts import redirect, render
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from accounts.forms import CustomUserCreationForm

# Create your views here.

def index(request):
    return render(request, 'accounts/index.html')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request,user) # 자동 로그인
            return redirect('accounts:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form':form
    }
    return render(request,'accounts/signup.html',context)

def login(request):
    if request.method == 'POST':
        form = AuthentionForm