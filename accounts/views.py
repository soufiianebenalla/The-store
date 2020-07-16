from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import HttpResponseBadRequest
from django.contrib.auth import get_user_model

from .forms import SignUpForm, UserProfileForm
from .utils import send_confirmation_email
from .tokens import confirm_email_token_generator

User = get_user_model()


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            user.is_active = False

            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()
            send_confirmation_email(request, user)

            return render(request, 'registration/signup_success.html')

    else:
        form = SignUpForm()
        profile_form = UserProfileForm()

    context = {'form': form, 'profile_form': profile_form}
    return render(request, 'registration/signup.html', context)


def activate_email(request, uid, token):
    user = get_object_or_404(User, pk=uid)
    if confirm_email_token_generator.check_token(user, token):
        user.is_active = True
        user.save()

        return redirect('login')
    else:
        return HttpResponseBadRequest('Bad Token')
