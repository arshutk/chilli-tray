from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, Paginator

from user_task.forms import RegistrationForm, LoginForm, TaskForm
from user_task.models import Task



def registration_view(request):
    ''' Registration View : handles the registration form submission and applies the model level validations '''

    context = {'title': 'Signup'}

    if request.user.is_authenticated:
        # redirecting user to home page if already authenticated
        return redirect('home')


    # POST request
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # redirecting user to home page on successfull signup
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            user = authenticate(username=username, password=password1)
            login(request, user)

            return redirect('home')
        else:
            context['form'] = form
    # GET request
    else:
        form = RegistrationForm()
        context['form'] = form
        
    return render(request, 'user_task/form.html', context)


def login_view(request):
    ''' Login View : Handles the login of user and on successfull login redirect them to home page'''

    user = request.user
    context = {'title': 'Login'}

    if user.is_authenticated:
        # redirecting user to home page if already authenticated
        return redirect('home')

    # POST request
    elif request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect('home')
        else:
            context['form'] = form

    #GET request
    else:
        form = LoginForm()
        context['form'] = form

    return render(request, 'user_task/form.html', context)


@(login_required(login_url='login'))
def logout_view(request):
    '''Logout View : Handles the logging out of the user'''

    logout(request)
    return redirect('login')



@(login_required(login_url='login'))
def home_view(request):
    ''' This view will display all the tasks created by a user'''

    page_num = request.GET.get('page', 1)   

    query = Task.objects.filter(user = request.user)
    tasks = Paginator(query, 5)

    try:
        paginated_tasks = tasks.page(page_num)
    except EmptyPage:
        paginated_tasks = tasks.page(1)

    return render(request, 'user_task/home.html', context={'tasks': paginated_tasks})


@(login_required(login_url='login'))
def task_create_view(request):
    ''' View for authenticated users to create tasks'''

    context = {}
    print(request.POST)
    # POST request
    if request.POST:
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect('home')
        else:
            context['form'] = form
    
    # GET request
    else:
        form = TaskForm()
        context['form'] = form
    
    return render(request, 'user_task/task_create.html', context)

