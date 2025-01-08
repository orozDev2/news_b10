from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password


class LoginForm(forms.Form):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Имя пользователя'
    }))

    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'Пароль'
    }))


class ChangePasswordForm(forms.Form):

    def __init__(self, *args, **kwargs):
        self.user: User = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    old_password = forms.CharField(label='Старый пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password = forms.CharField(label='Новый пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                                   validators=[validate_password])
    confirm_password = forms.CharField(label='Подтвердите пароль',
                                       widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self):
        if self.is_valid():
            old_password, new_password, confirm_password = self.cleaned_data.values()

            errors = {}

            if not self.user.check_password(old_password):
                errors['old_password'] = ['The old password is incorrect.']

            if new_password != confirm_password:
                errors['confirm_password'] = ['The passwords are not matches.']

            if old_password == new_password:
                errors['new_password'] = ['The new password should not be old password.']

            if len(errors) > 0:
                raise forms.ValidationError(errors)

        return self.cleaned_data


class RegisterForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True

    password1 = forms.CharField(label='Придумайте пароль',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                                validators=[validate_password])

    password2 = forms.CharField(label='Придумайте пароль',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
        )

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        if self.is_valid():

            password1 = self.cleaned_data.get('password1')
            password2 = self.cleaned_data.get('password2')

            if password1 != password2:
                raise forms.ValidationError({'password2': ['Пароли не совпадают']})

        return self.cleaned_data
