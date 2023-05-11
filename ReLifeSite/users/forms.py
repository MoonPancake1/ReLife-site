from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Nov, Account, Mod
from django.forms import ModelForm, TextInput, Textarea, Select, FileInput, CheckboxInput, PasswordInput

User = get_user_model()


class UserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email"}),
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")


class AddUserInCreditsForms(ModelForm):
    class Meta:
        model = Account
        fields = ["nick_in_credits"]
        widgets = {
            "nick_in_credits": TextInput(attrs={
                "class": "form-control text-center form-control-lg",
                "type": "text",
                "placeholder": "Ник/Имя",
                "aria-label": "Ник/Имя",
                "aria-describedby": "basic-addon1",
            }),
        }


class EditUserAccountForm(ModelForm):
    class Meta:
        model = Account
        fields = ["img", "first_name", "last_name",
                  "birthday", "gender", "phone",
                  "web_site", "github", "telegram",
                  "discord"]

        widgets = {
            "img": FileInput(attrs={
                "class": "form-control",
                "type": "file",
                "id": "formFile",
            }),
            "first_name": TextInput(attrs={
                "class": "form-control",
                "type": "text",
                "placeholder": "Имя",
                "aria-label": "Имя",
                "aria-describedby": "basic-addon1",
            }),
            "last_name": TextInput(attrs={
                "class": "form-control",
                "type": "text",
                "placeholder": "Фамилия",
                "aria-label": "Фамилия",
                "aria-describedby": "basic-addon1",
            }),
            "birthday": TextInput(attrs={
                "class": "form-control",
                "type": "date",
                "placeholder": "День рождения",
                "aria-label": "День рождения",
                "aria-describedby": "basic-addon1",
            }),
            "gender": Select(attrs={
                "class": "form-select",
                "aria-label": "Пол",
                "name": "gender",
                "id": "id_gender",
            }),
            "phone": TextInput(attrs={
                "class": "form-control",
                "type": "text",
                "placeholder": "Моб. телефон",
                "aria-label": "Моб. телефон",
                "aria-describedby": "basic-addon1",
            }),
            "web_site": TextInput(attrs={
                "class": "form-control",
                "type": "text",
                "placeholder": "Веб-сайт",
                "aria-label": "Веб-сайт",
                "aria-describedby": "basic-addon1",
            }),
            "github": TextInput(attrs={
                "class": "form-control",
                "type": "text",
                "placeholder": "GitHub",
                "aria-label": "GitHub",
                "aria-describedby": "basic-addon1",
            }),
            "telegram": TextInput(attrs={
                "class": "form-control",
                "type": "text",
                "placeholder": "Telegram",
                "aria-label": "Telegram",
                "aria-describedby": "basic-addon1",
            }),
            "discord": TextInput(attrs={
                "class": "form-control",
                "type": "text",
                "placeholder": "Discord",
                "aria-label": "Discord",
                "aria-describedby": "basic-addon1",
            }),
        }


class NovForm(ModelForm):
    class Meta:
        model = Nov
        fields = ["title", "description", "description_comp",
                  "author", "link_news", "img"]
        widgets = {
            "title": TextInput(attrs={
                "name": "title",
                "class": "form-control vTextField",
                "maxlength": "255",
                "type": "text",
                "id": "id_title",
                "required": "",
                "placeholder": "Яблоко упало",
            }),
            "description": Textarea(attrs={
                "name": "description",
                "cols": "40",
                "rows": "6",
                "class": "form-control vLargeTextField",
                "id": "id_description",
                "required": "",
                "placeholder": "Сегодня утром упало зелёное яблоко",
            }),
            "description_comp": TextInput(attrs={
                "class": "form-control vTextField",
                "type": "text",
                "id": "id_description_comp",
                "name": "description_comp",
                "maxlength": "255",
                "required": "",
                "placeholder": "Упало зелёное яблоко",
            }),
            "author": TextInput(attrs={
                "class": "form-control vTextField",
                "type": "text",
                "id": "id_author",
                "name": "author",
                "maxlength": "255",
                "required": "",
                "placeholder": "Яблоко",
            }),
            "img": FileInput(attrs={
                "class": "form-control",
                "type": "file",
                "id": "formFile",
            }),
            "link_news": TextInput(attrs={
                "type": "text",
                "class": "form-control vTextField",
                "id": "id_link_news",
                "aria-describedby": "basic-addon3",
                "name": "link_news",
                "maxlength": "255",
                "required": "",
            }),
        }


class ModForm(ModelForm):
    class Meta:
        model = Mod
        fields = ["title", "description", "author",
                  "img_mod", "mod"]
        widgets = {
            "title": TextInput(attrs={
                "name": "title",
                "class": "form-control vTextField",
                "maxlength": "255",
                "type": "text",
                "id": "id_title",
                "required": "",
                "placeholder": "Падение яблок",
            }),
            "description": Textarea(attrs={
                "name": "description",
                "cols": "40",
                "rows": "6",
                "class": "form-control vLargeTextField",
                "id": "id_description",
                "required": "",
                "placeholder": "Замечательная история про яблоки",
            }),
            "author": TextInput(attrs={
                "class": "form-control vTextField",
                "type": "text",
                "id": "id_author",
                "name": "author",
                "maxlength": "255",
                "required": "",
                "placeholder": "Команда или человек",
            }),
            "img_mod": FileInput(attrs={
                "class": "form-control",
                "type": "file",
                "id": "formFile",
            }),
            "mod": FileInput(attrs={
                "class": "form-control",
                "type": "file",
                "id": "formFile",
            }),
        }
