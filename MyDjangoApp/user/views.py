from ssl import AlertDescription
from urllib import request
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm
from django.core.mail import send_mail








def register_user(request):
  if request.method ==  "POST":
    form = RegisterUserForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password1')
      messages.success(request, 'Account was created for ' + username)
      return redirect('login')
  else:
    form = RegisterUserForm()
      
  return render(request, 'authenticate/register_user.html', {'form': form})    






def logout_user(request):
    logout(request)
    return redirect('login')





def login_user(request):
  
  
    if request.method == 'POST':
      username = request.POST.get('username')
      password = request.POST.get('password')
      user = authenticate(request, username=username, password=password)
      if user is not None:
        login(request, user)
        return redirect('home')
      else:
        messages.info(request, 'Username OR password is incorrect')
    return render(request, 'authenticate/login.html')
  
  
  
    
    
  