from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin

from users.froms import UserLoginForm, UserRegistrationForm, UserProfileForm
from products.models import Basket
from users.models import User
from common.views import TitleMixin


class UserLoginView(TitleMixin, LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    title = 'Store - Авторизация'


class UserRegistrationView(SuccessMessageMixin, TitleMixin, CreateView):
    model = User
    form_class = UserRegistrationForm
    title = 'Store - Регистрация'
    template_name = 'users/registration.html'
    success_url = reverse_lazy('users:login')
    success_message = 'Поздравляем! Вы успешно зарегестрированы!'


class UserProfileView(TitleMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    title = 'Store - Личный кабинет'
    template_name = 'users/profile.html'

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.object.id,))

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['baskets'] = Basket.objects.filter(user=self.object)
        return context
