from django import forms
from .models import SignUp


class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        widgets = {'password': forms.PasswordInput()}
        fields = ['email', 'first_name', 'last_name', 'password']

    def clean_password(self):
        password = self.cleaned_data.get('password')

        if len(password) < 5:
            raise forms.ValidationError("Password must be more than 5 characters")
        if len(password) > 50:
            raise forms.ValidationError("Password must be less than 50 characters")

        return password

