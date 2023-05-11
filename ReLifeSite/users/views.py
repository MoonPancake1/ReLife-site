from ReLifeSite.settings import BASE_DIR
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.views import View

from .forms import *
from .models import *
from .imageEditor import crop_image


def index(request):
    ip = get_client_ip(request)
    return render(request, 'users/index.html',
                  context={'ip': ip})


# Ошибка 404. Error 404 Not Founded
def error_404_view(request, exception):
    # we add the path to the 404.html file
    # here. The name of our HTML file is 404.html
    return render(request, 'users/404.html')


def about(request):
    return render(request, 'users/about.html')


def user_agreement(request):
    return render(request, 'users/user_agreement.html')


def privacy_policy(request):
    return render(request, 'users/privacy_policy.html')


def info(request):
    return render(request, 'users/info_page.html')


def account(request):
    return render(request, 'users/account/account.html')


def add_nick_in_credits(request):
    user = request.user.account
    form = AddUserInCreditsForms(instance=user)

    if request.method == 'POST':
        form = AddUserInCreditsForms(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('lk')

    context = {
        'form': form,
    }
    return render(request, 'users/account/account_add_nick_credits.html', context)


def account_check(request, username):
    user_data = User.objects.get(username=username)
    context = {
        'user_data': user_data
    }
    return render(request, 'users/account/account_view.html', context)


def edit_account(request):
    user = request.user.account
    form = EditUserAccountForm(instance=user)

    if request.method == 'POST':
        form = EditUserAccountForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            # crop_image(f'{request.FILES["img"]}')
            return redirect('lk')

    context = {
        'form': form,
    }
    return render(request, 'users/account/account_edit.html', context)


def news(request):
    news = Nov.objects.order_by('-date')
    return render(request, 'users/link_news/news.html', {'nov': news})


class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm(),
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        error = {}
        ip = get_client_ip(request)

        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            group = Group.objects.get(name='account')
            user.groups.add(group)
            Account.objects.create(user=user)
            Account.objects.filter(user=user).update(ip_address=ip)

            user = authenticate(username=username,
                                password=password)
            login(request, user)
            print(f'Пользователь успешно зарегистрирован! - {form.cleaned_data.get("email")}:{password}')
            return redirect('home')
        else:
            pass

        for i in form.errors:
            if i == 'email':
                error['email'] = 'Введена некорректная почта!'
            elif i == 'username':
                error['username'] = 'Пользователь с таким ником уже существует!'
            elif i == 'password2':
                error['password2'] = 'Проверте правильность ввода пароля, возможно он слабый.'

        context = {
            'form': form,
            'error': error,
        }
        return render(request, self.template_name, context)


def news_base(request, title_news):
    des_news = Nov.objects.get(link_news=title_news)

    ip = get_client_ip(request)
    if Ip.objects.filter(ip=ip).exists():
        des_news.views.add(Ip.objects.get(ip=ip))
    else:
        Ip.objects.create(ip=ip)
        des_news.views.add(Ip.objects.get(ip=ip))

    p_tag = des_news.description.split("\r\n")
    # Удалить
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    ip = request.META.get('REMOTE_ADDR')
    context = {
        'news': des_news,
        'x_forwarded_for': x_forwarded_for,
        'ip': ip,
        'p_tag': p_tag,
    }
    return render(request, 'users/link_news/base_news.html', context)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def edit_news(request, title_news):
    error = ''
    des_news = Nov.objects.get(link_news=title_news)
    form = NovForm(instance=des_news)

    if request.method == 'POST':
        form = NovForm(request.POST, request.FILES, instance=des_news)
        if form.is_valid():
            form.save()
            return redirect('news')
        else:
            error = 'Форма некорректна!'

    context = {
        'form': form,
        'news': des_news,
    }
    return render(request, 'users/link_news/edit_news.html', context)


def create_news(request):
    error = ''
    if request.method == 'POST':
        form = NovForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('news')
        else:
            error = 'Новость заполнена неправильно!'

    form = NovForm()
    context = {
        'form': form,
        'error': error,
    }
    return render(request, 'users/link_news/create_news.html', context)


def del_news(request, title_news):
    des_news = Nov.objects.get(link_news=title_news)
    if request.method == "POST":
        des_news.delete()
        return redirect('news')

    context = {
        'news': des_news,
    }
    return render(request, 'users/link_news/del_news.html', context)


# Рендер страниц: Модификации
def mod_main(request):
    mods = Mod.objects.order_by('-date')
    return render(request, 'users/modifications/modifications_main.html',
                  {
                      'mods': mods
                  })


def mod_create(request):
    error = ''
    if request.method == 'POST':
        form = ModForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('modifications')
        else:
            error = 'Возникла ошибка!'

    form = ModForm()
    context = {
        'form': form,
        'error': error,
    }
    return render(request, 'users/modifications/modifications_create.html', context=context)


def mod_edit(request):
    return render(request, 'users/modifications/modifications_edit.html')


def mod_info(request):
    return render(request, 'users/modifications/modifications_info.html')
