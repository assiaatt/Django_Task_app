from .models import Task
from .forms import TaskForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.decorators import login_required


# Create your views here.

# def main(request):
#     template = loader.get_template('main.html')

#     return HttpResponse(template.render())

# def login(request):

#     template = loader.get_template('login.html')

#     return HttpResponse(template.render())

# def register(request):
#     form = UserCreationForm()

#     if request.method == 'POST':
#         form = UserCreationForm(request.form)
#         if form.is_valid():
#             form.save()

#     context = {'form':form}

#     return render(request,'register.html')

######### user def 

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('task_list')  # Redirect to the task list page
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


def custom_logout(request):
    logout(request)
    return redirect('login') 




################ task def

@login_required
def task_list(request):
    
    tasks = Task.objects.filter(user=request.user)

    status = request.GET.get('status')
    

    if status:
        tasks = tasks.filter(status=status)
    
    
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_detail', pk=task.pk)
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})

@login_required
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'tasks/task_detail.html', {'task': task})

@login_required
def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_detail', pk=task.pk)
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})

@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('task_list')
