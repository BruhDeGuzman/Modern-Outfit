from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm

# Here are the views which take a request and return a response.

def register(request):
    """ a view that responsible fro Registration of users """

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}, Your account is created')
            return redirect('products:index')

    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form':form})
