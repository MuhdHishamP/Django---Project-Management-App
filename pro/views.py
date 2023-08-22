from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .forms import SignUpForm,Pro_add_form
from .models import Pro_add
# Create your views here.
def home(request):
    Pro_add_details = Pro_add.objects.all()
    form = Pro_add_form()
    #for logging in
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'add_record':
            if form.is_valid():
                form.save()
                messages.success(request, "Record Added...")
                return redirect('home')
        else:    
            username = request.POST['username']
            password = request.POST['password']
            # for authenticating
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request, user)
                messages.success(request,'You have been logged in...')
                return redirect('home')
            else:
                messages.error(request,'Error occured, Try again...')
                return redirect('home')
    else:
        return render(request,'home.html',{'Pro_add_details':Pro_add_details,'form':form})
"""def pro_add(request):
    Pro_add_details = Pro_add.objects.all()
    form = Pro_add_form()
    return render(request, 'home.html',{'Pro_add_details':Pro_add_details,'form':form})"""

def logout_user(request):
    logout(request)
    messages.success(request,'You have been logged out...')
    return redirect('home')
def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username,password = password)
            login(request, user)
            messages.success(request,"You Have Successfully Registered")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html',{'form':form})
    return render(request,'register.html',{'form':form})

