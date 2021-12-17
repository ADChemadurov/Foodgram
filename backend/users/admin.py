from django import forms
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.models import Group
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class UserCreationForm(forms.ModelForm):
    """
    Переопределяет форму создания пользователя, добавляет в нее поля:
    email, first_name, last_name.
    Поля password1, password2 необходимо указать иначе
    они не будут отражаться в представлении.
    """
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Подтверджение пароля', widget=forms.PasswordInput,
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError('Пароли не совпадают!')
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):

    password = ReadOnlyPasswordHashField(
        label=_('Пароль'),
        help_text=_(
            'Пароли шифруются, поэтому нет возможности увидеть его.'
            'Однако, можно его изменить, используя '
            '<a href={}>эту форму</a>.'
        ),

    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        password = self.fields.get('password')
        if password:
            password.help_text = password.help_text.format('../password/')
        user_permissions = self.fields.get('user_permissions')
        if user_permissions:
            user_permissions.queryset = (
                user_permissions.queryset.select_related('content_type'))

    class Meta:
        fields = (
            'username',
            'email',
            'password',
            'first_name',
            'last_name',
            'is_admin'
        )

    def clean_password(self):
        return self.initial["password"]

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    add_fieldsets = (
        (None, {
            'fields': (
                'email',
                'username',
                'first_name',
                'last_name',
                'password1',
                'password2',
            ),
        }),
    )
    list_display = ('id', 'username', 'email', 'first_name', 'last_name',)


admin.site.unregister(Group)
