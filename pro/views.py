from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .forms import SignUpForm,Pro_add_form,task_add_form
from .models import Pro_add,task_add
from django.urls import reverse
from datetime import datetime




# Create your views here.
def home(request):
    Pro_add_details = Pro_add.objects.all()
    form = Pro_add_form(request.POST or None)
    now = datetime.today().date()   
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
        return render(request,'home.html',{'Pro_add_details':Pro_add_details,'form':form,'now':now})


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
        # return render(request, 'register.html',{'form':form})
    return render(request,'register.html',{'form':form})
def delete_project(request , pk):
    item = Pro_add.objects.get(id=pk)
    if request.method=="POST":
        item.delete()
        messages.success(request, "Record Deleted Successfully")

        return redirect('home')
def tasks(request, pk):
    open = get_object_or_404(Pro_add, id=pk)
    open_tasks = task_add.objects.filter(open=open)
    pro_add_instance = Pro_add.objects.get(id=pk) 
    oldform = Pro_add_form(instance=pro_add_instance)
    form = task_add_form(request.POST or None)
    selected_task_ids = [] 

    if request.method == "POST":
        action = request.POST.get('action')
        
        if action == 'add_task':
            if form.is_valid():
                task = form.cleaned_data['task']
                tas = task_add(open=open, task=task)
                tas.save() 
                messages.success(request, "Task Added...")
            else:
                messages.error(request, "Task could not be added. Please fill in the required field.")
        
        elif action == 'delete_tasks':
            task_ids = request.POST.getlist('task_ids')
            tasks_to_delete = task_add.objects.filter(id__in=task_ids)
            tasks_to_delete.delete()
            messages.success(request, "Selected Tasks Deleted.")
        
        selected_task_ids = request.POST.getlist('task_ids', [])


        tasks_list_url = reverse('tasks', args=[pk])
        return redirect(tasks_list_url)

    
    else:
        context = {
            'oldform': oldform,
            'form': form,
            'open_tasks': open_tasks,
            'selected_task_ids': selected_task_ids,  # Pass the selected task IDs to the template
            'open': open,
        }
        return render(request, 'task.html', context)