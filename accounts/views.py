from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import UserLoginForm, UserRegistrationForm


def index(request):
    """Loads index.html"""
    return render(request, 'index.html')
  
  
@login_required    
def logout(request):
    """Logs the user out"""
    auth.logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect(reverse('index'))
    
    
def login(request):
    """Return a page for the user to log in"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                        password=request.POST['password'])
                                        
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in")
                return redirect(reverse('members_home'))
            else: 
                login_form.add_error(None, "Your username or password is incorrect")
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {"login_form": login_form})
    

def registration(request):
    """Returns a page where the user can register"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))
         
    if request.method =="POST":
        registration_form = UserRegistrationForm(request.POST)
        
        if registration_form.is_valid():
            registration_form.save()
            user = auth.authenticate(username=request.POST['username'], 
                                        password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('index'))
            else:
                messages.error(request, "Unable to register your account at this time")
    else:
        registration_form = UserRegistrationForm()
            
    
    return render(request, 'registration.html', 
        {"registration_form": registration_form} )


@login_required
def members_home(request):
    """Returns the signed in member's home page"""
    user = User.objects.get(email=request.user.email)
    return render(request, 'membershome.html', {"profile": user})
    
    
def non_members_home(request):
    # Returns a page explaining the benefits of signing up, if the user hasn't already
    return render(request, 'nonmembershome.html')

def about_page(request):
    # Renders an about page
    return render(request, 'about.html')