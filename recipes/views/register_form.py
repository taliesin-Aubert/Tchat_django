from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import reverse
from django.views import generic

from recipes.forms.register import RegisterForm


class RegisterFormView(generic.FormView):
    template_name = 'index.html'
    form_class = RegisterForm

    def form_valid(self, form):
        user = form.cleaned_data['user']
        Msg = form.cleaned_data['Msg']
        try:
            User.objects.create_user(
                user=user, Msg=Msg
            )
            messages.add_message(
                self.request, messages.INFO,
                'Message created successfully.'
            )
        except Exception as e:
            form.add_error(None, "Unexpected error")
            return super().form_invalid(form)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('index')
