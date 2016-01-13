from django import forms
from .models import Account


class SignUpForm(forms.ModelForm):
    class Meta:

        model = SignUp
        widgets = {
            'password': forms.PasswordInput(),
        }
        fields = ['email', 'first_name', 'last_name', 'password', 'thumbnail']

    def clean_password(self):
        password = self.cleaned_data.get('password')

        if len(password) < 5:
            raise forms.ValidationError("Password must be more than 5 characters")
        if len(password) > 50:
            raise forms.ValidationError("Password must be less than 50 characters")
        return password


    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and Account.objects.filter(email=email).count():
            raise forms.ValidationError('This email address has already been used.')
        return email