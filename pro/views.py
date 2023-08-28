from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .forms import SignUpForm,Pro_add_form,task_add_form
from .models import Pro_add,task_add
from django.urls import reverse



# Create your views here.
def home(request):
    Pro_add_details = Pro_add.objects.all()
    form = Pro_add_form(request.POST or None)
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'add_record':
            if form.is_valid():
                form.save()
                messages.success(request, "Record Added...")
                return redirect('home')
            else:
                messages.error(request, "Please complete all the fields...")
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
def update_project(request, pk):
    pro_add_instance = Pro_add.objects.get(id=pk)  # Retrieve the instance
    if request.method == 'POST':
        form = Pro_add_form(request.POST, instance=pro_add_instance)  # Populate the form with instance data
        if form.is_valid():
            form.save()
            messages.success(request, "Record Updated Successfully")
            #return redirect('home')
    else:
        form = Pro_add_form(instance=pro_add_instance)  # Populate the form with instance data
    return render(request, 'update_project.html', {'form': form, 'pro_add_instance': pro_add_instance})
def delete_project(request , pk):
    item = Pro_add.objects.get(id=pk)
    if request.method=="POST":
        item.delete()
        messages.success(request, "Record Deleted Successfully")

        return redirect('home')
def task(request ,pk):
    open = get_object_or_404(Pro_add,id = pk)
    open_tasks = open.task_add.all()
    form = task_add_form()
    if request.method == "POST":
        form = task_add_form(request.POST) 
        if form.is_valid():
            form.save() 
            messages.success(request, "Task Added...")
            task_list_url= reverse('task', args=[pk])
            return redirect('task')

    else:
        return render(request, 'task.html',{'form':form,'open_tasks':open_tasks,'open':open})   
    return render(request, 'task.html',{'form':form,'open_tasks':open_tasks,'open':open})   
