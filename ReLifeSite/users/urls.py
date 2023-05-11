from django.urls import path, include
from . import views
from .views import Register

urlpatterns = [
    path('', views.index, name='home'),
    path('users', include('django.contrib.auth.urls')),
    path('registration', Register.as_view(), name='register'),
    path('about', views.about, name='about'),

    # Модификации к игре
    path('modifications', views.mod_main, name='modifications'),
    path('modifications_create', views.mod_create, name='modifications_create'),
    path('modifications_edit', views.mod_edit, name='modifications_edit'),
    path('modifications_info', views.mod_info, name='modifications_info'),

    # Документы
    path('user_agreement', views.user_agreement, name='user_agreement'),
    path('privacy_policy', views.privacy_policy, name='privacy_policy'),
    path('info_relife', views.info, name='info'),

    # Аккаунты
    path('account', views.account, name='lk'),
    path('account_<str:username>', views.account_check, name='a_c'),
    path('account/edit', views.edit_account, name='edit_account'),
    path('account/add_nick', views.add_nick_in_credits, name='a_n_i_c'),

    # Новости
    path('news', views.news, name='news'),
    path('create_news', views.create_news, name='c_n'),
    path('news/<str:title_news>', views.news_base, name='news_base'),
    path('news/news_edit/<str:title_news>', views.edit_news, name='news_edit'),
    path('news/news_del/<str:title_news>', views.del_news, name='news_del'),

]


