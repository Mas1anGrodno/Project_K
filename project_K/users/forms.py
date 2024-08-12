from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model

class LoginUserForm (AuthenticationForm):
    username = forms.CharField(label = 'Логин', widget=forms.TextInput(attrs={'class':'forms-input'}), max_length=255, required=False)
    password = forms.CharField(label = 'Пароль', widget=forms.PasswordInput(attrs={'class':'forms-input'}), max_length=255, required=False)
    class Meta:
        model = get_user_model()
        fields = ['username', 'password']