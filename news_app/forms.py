from django import forms
from django.contrib.auth import authenticate


class LoginForm(forms.Form):
    username = forms.CharField(label='',
                               widget=forms
                               .TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(label='',
                               widget=forms
                               .PasswordInput(attrs={'placeholder':
                                                     'Password'}))

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError(
                "Either your username or password is invalid.")
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user
