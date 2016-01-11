from django import forms
from .models import Account


class SignUpForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['email', 'first_name', 'last_name']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and Account.objects.filter(email=email).count():
            raise forms.ValidationError('This email address has already been used.')
        return email