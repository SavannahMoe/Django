from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save() #creat new user from that form
            login(request,new_user) #log in immediately
            return redirect('MainApp:index')

    context = {'form': form}
    return render(request, 'registration/register.html', context)