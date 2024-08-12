from django import forms

class LoginUserForm (forms.Form):
    username = forms.CharField(label = 'Логин', widget=forms.TextInput(attrs={'class':'forms-input'}), max_length=255, required=False)
    password = forms.CharField(label = 'Пароль', widget=forms.PasswordInput(attrs={'class':'forms-input'}), max_length=255, required=False)