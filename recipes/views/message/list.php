from django.views.generic import DetailView

from recipes.models.Msg_Tchat import Msg_Tchat


class MessageDetailView(DetailView):
    template_name = 'index.html'
    model = Msg_Tchat
