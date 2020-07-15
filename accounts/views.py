from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.db import transaction

from .forms import SignUpForm, ProfileForm
from .utils import send_confirmation_email
from .tokens import confirm_email_token_generator

User = get_user_model()


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            user.is_active = False
            user.save()
            send_confirmation_email(request, user)

            return render(request, 'registration/signup_success.html')
    else:
        form = SignUpForm()

    context = {'form': form, }
    return render(request, 'registration/signup.html', context)


def activate_email(request, uid, token):
    user = get_object_or_404(User, pk=uid)
    if confirm_email_token_generator.check_token(user, token):
        user.is_active = True
        user.save()

        return redirect('login')
    else:
        return HttpResponseBadRequest('Bad Token')


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
