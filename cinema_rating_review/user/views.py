from django.shortcuts import render, redirect
from django.contrib import messages
from . forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Your account has been activated, you can login!')    ## removed f
            return redirect('login')      # this must redirect to login
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})