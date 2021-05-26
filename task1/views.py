from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from task1.forms import RegistrationForm, LoginForm



def registration_view(request):
    ''' Registration View : handles the registration form submission and applies the model level validations '''

    context = {}
    # POST request
    if request.POST:
        form = RegistrationForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']

            # redirecting user to home page on successfull signup
            user = authenticate(username=username, password=password1)
            login(request, user)

            return redirect('home')
        else:
            context['form'] = form
    # GET request
    else:
        form = RegistrationForm()
        context['form'] = form
        
    return render(request, 'registration.html', context)


def login_view(request):
    ''' Login View : Handles the login of user and on successfull login redirect them to home page'''

    user = request.user
    context = {}

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
    return render(request, 'login.html', context)


def logout_view(request):
    '''Logout View : Handles the logging out of the user'''

    logout(request)
    return redirect('login')


def home_view(request):
    return render(request, 'home.html', context={})
