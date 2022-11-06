from django.shortcuts import redirect, render, HttpResponseRedirect
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib import messages

from account.models import UserBase

from .forms import RegistrationForm, UserEditForm, UserLoginForm
from .token import account_activation_token


def account_register(request):

    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        registerForm = RegistrationForm(request.POST)
        if registerForm.is_valid():
            user = registerForm.save(commit=False)
            user.email = registerForm.cleaned_data['email']
            user.set_password(registerForm.cleaned_data['password'])
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate your Account'
            message = render_to_string('account/registration/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject=subject, message=message)
            messages.success(
                request, "Tasdiqlovchi link elektron pochtangizga jo'onatildi!")

    else:
        registerForm = RegistrationForm()
    return render(request, 'account/registration/register.html', {'form': registerForm})


def account_activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = UserBase.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, user.DoesNotExists):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('/')
    else:
        return render(request, 'account/registration/activation_invalid.html')


def login_user(request):
    form = UserLoginForm()
    if request.method == 'POST':
        login_form = UserLoginForm(data=request.POST)
        print(login_form.is_valid())
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
        else:
            messages.error(request, 'Email yoki parol xato!')
            return redirect('account:login')

    content = {
        'form': form,
        'next': next,
    }

    return render(request, 'account/login.html', content)


def logout_view(request):
    logout(request)
    return redirect('/')


@login_required
def delete_user(request, pk):
    user = UserBase.objects.get(pk=pk)
    user.is_active = False
    user.save()
    logout(request)
    messages.success(request, "Accountingiz o'chirildi")
    return redirect('account:register')


@login_required
def edit_details(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)

        if user_form.is_valid():
            user_form.save()
        messages.success(request, "Ma'lumotlaringiz o'zgartirildi!")
    else:
        user_form = UserEditForm(instance=request.user)

    return render(request, 'account/edit_details.html', {'user_form': user_form})
