from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . forms import UserRegistrationForm, UserUpdateForm

# Register User view
def register(request):

    if request.method == 'POST':
        
        form = UserRegistrationForm(request.POST)
        if form.is_valid():

            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account creation successful! You may log in.')
            return redirect('login')
        else: 
            form = UserRegistrationForm()
        return redirect(request, 'users/register.html', {'form': form})

# Go to the user's profile
@login_required
def profile(request):

    template_name = 'users/profile.html'

    if request.method == 'POST':

        u_form = UserUpdateForm(request.POST, instance=request.user)
        
        if u_form.is_valid():

            u_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('profile')
    else:
        # Instance = current logged in user
        u_form = UserUpdateForm(instance=request.user)
        
    context = {
        'u_form': u_form
    }

    return render(request, template_name, context)