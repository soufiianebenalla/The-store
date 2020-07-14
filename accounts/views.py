from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import transaction

from .forms import SignUpForm, ProfileForm


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('login')
    else:
        form = SignUpForm()

    context = {'form': form, }
    return render(request, 'registration/signup.html', context)


@login_required
@transaction.atomic
def update_profile(request):

    if request.method == 'POST':

        signup_form = SignUpForm(request.POST)
        profile_form = ProfileForm(request.POST)

        if signup_form.is_valid() and profile_form.is_valid():
            signup_form.save()
            profile_form.save()
            messages.success(request, _(
                'Your profile was successfully updated!'))
            return redirect('login')
        else:
            messages.error(request, _('Please correct the error below.'))

    else:
        signup_form = SignUpForm()
        profile_form = ProfileForm()

    context = {
        'signup_form': signup_form,
        'profile_form': profile_form
    }

    return render(request, 'registration/signup.html', context)
