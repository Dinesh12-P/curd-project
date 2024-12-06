from django.shortcuts import render,redirect
from .models import *
from store.forms import *
from django.contrib import messages
from store.forms import * 
from django.contrib.auth  import login, logout, authenticate 
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def hero(request):
    return render(request,'store/main.html')

def table(request):
    if 'q' in request.GET:
        q = request.GET['q']
        tasks = Task.objects.filter(title__icontains=q)
    else:
       tasks = Task.objects.all()

    if not tasks.exists():
        tasks = Task.objects.all()
    
    # tasks = Task.objects.all()
    context = {
        'tasks':tasks,
        'Total_Task':len(tasks),
        'Completed_Task':tasks.filter(status=True).count(),
        'Incompleted_Task':tasks.filter(status=False).count(),
    }
    
    return render(request, 'store/table.html', context)
class CreateTaskView(CreateView):
    models = Task
    form_class=diform
    template_name = 'store/create_task.html'
    success_url = '/'


def create_task(request):
  if request.method =='POST':
     title = request.POST.get('title')
     description = request.POST.get('description')

     Task.objects.create(title=title,description=description)
     messages.success(request,"Task created successfully!!")
          
     return redirect('table')

  return render(request,'store/create_task.html')
def scroll(request):
    return render(request,'store/scroll.html' )

def mark(request, pk):
   task = Task.objects.get(pk=pk)
   task.status = True
   task.save()
   return redirect('table')

def unmark(request, pk):
   task = Task.objects.get(pk=pk)
   task.status = False
   task.save()
   return redirect('table')

 

def delete(request, pk):
   task = Task.objects.get(pk=pk)
   task.delete()
   task.delete
   messages.success(request,"Task deleted successfully!!")
   
   return redirect('table')

# class UpdateTaskView(UpdateView):
#     model = Task
#     form_class=diform
#     template_name='store/update_task.html'
#     success_url='table'
def update_Task(request, pk):
    
    task = Task.objects.get(pk=pk)
    if request.method== 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        
        task.title =title
        task.description = description    
    
        task.save()
        messages.success(request,"Task updated successfully!!")

        return redirect('table')
    
    context = {
        'task':task,
    }
    
    return render(request, 'store/update_task.html', context)

def pricing(request):
   return render(request,'store/pricing.html')

def form_create(request):
    if request.method == 'POST':
        form = diform(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('table')
    else:
        form = diform 
        
    return render(request,'store/form.html',{'form':form})

def dinesh(request):
      return render(request,'store/dinesh.html')

def register_form(request):
 if request.method=='POST':
    form = RegisterForm(request.POST)
    if form.is_valid(): 
        user= form.save()

        return redirect('login')
 else:
    form = RegisterForm()
        
 return render(request,'store/register.html',{'form':form})

def login_form(request):
    if request.method=='POST':
      form = LoginForm(request.POST)
      
   
      if form.is_valid():
         username=form.cleaned_data['username']
         password=form.cleaned_data['password']

         user = authenticate(request, username=username, password=password)

         if user is not None:
            login(request, user)
            messages.success(request, "Successfully logged in")
         return redirect('table')
    else:
            form = LoginForm()

    return render(request, 'store/login.html',{'form':form})
def logout_form(request):
   logout(request)
   messages.success(request,'Successfully Logged Out')
   return redirect ('login')

def view_details(request, pk):
   task = Task.objects.get(pk=pk)
   return render(request, 'store/view_details.html',{'task':task})
         



    # students = [
    #     {
    #         'sno':1,
    #         'name':'Dipen',
    #         'age':2,
    #         'gender':'Male'
    #     },
    #     {
    #         'sno':2,
    #         'name':'Perry',
    #         'age':12,
    #         'gender':'Female'
    #     },
    #     {
    #         'sno':3,
    #         'name':'Virat',
    #         'age':45,
    #         'gender':'Male'
    #     },
    #     {
    #         'sno':4,
    #         'name':'Amelia',
    #         'age':1,
    #         'gender':'Female'
    #     },

    # ]


