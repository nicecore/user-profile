from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from . import models
from . import forms


def sign_in(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            if form.user_cache is not None:
                user = form.user_cache
                if user.is_active:
                    login(request, user)
                    return redirect('accounts:profile')
                else:
                    messages.error(
                        request,
                        "That user account has been disabled."
                    )
            else:
                messages.error(
                    request,
                    "Username or password is incorrect."
                )
    return render(request, 'accounts/sign_in.html', {'form': form})


def sign_up(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )
            login(request, user)
            messages.success(
                request,
                "You're now a user! You've been signed in, too."
            )
            return HttpResponseRedirect(reverse('home'))  # TODO: go to profile
    return render(request, 'accounts/sign_up.html', {'form': form})


def sign_out(request):
    logout(request)
    messages.success(request, "You've been signed out. Come back soon!")
    return HttpResponseRedirect(reverse('home'))


@login_required
def show_profile(request):

    # Get profile
    profile = request.user.userprofile

    # Render the template and pass it the profile in a context dict
    return render(request, 'accounts/profile.html', {'profile': profile})


@login_required
def edit_profile(request):
    form = forms.UserProfileForm(instance=request.user.userprofile)
    if request.method == 'POST':
        form = forms.UserProfileForm(data=request.POST, instance=request.user.userprofile, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/accounts/profile')
    return render(request, 'accounts/edit_profile.html', {'form': form})


@login_required
def change_pw(request):

    # If the request coming into this view has a POST method...

    if request.method == 'POST':
        # Set form to PasswordChangeForm and pass it the user and the POST
        form = PasswordChangeForm(request.user, request.POST)
        # Validate form
        if form.is_valid():
            # Save form
            user = form.save()
            # Ensure user's session won't be invalidated/user won't be
            # required to log in again
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/accounts/profile')
        else:
            messages.error(request, 'Please fix the error')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {'form': form})











