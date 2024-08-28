import random
import secrets
import string

from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, TemplateView

from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterView
from users.models import User


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterView
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email-confirm/{token}/'
        send_mail(
            subject='Подтверждение почты',
            message=f'Перейдите по ссылке для подтверждения своей почты: {url}',
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        return super().form_valid(form)


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))


def recovery_pass(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = get_object_or_404(User, email=email)
        password = ''.join(random.choice(string.ascii_letters) for _ in range(12))
        #hash_password = make_password(password)
        user.set_password(password)
        user.save()
        send_mail(
            subject='Сброс пароля',
            message=f' Ваш новый пароль {password}',
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        return redirect(reverse('users:login'))
    return render(request, 'recovery.html')



