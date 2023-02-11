from django import forms


class RegisterForm(forms.Form):
    user = forms.CharField(label="User", min_length=1, max_length=20,)
    Msg = forms.EmailField(label="Msg", min_length=1, max_length = 300)
