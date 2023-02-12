from django.http import JsonResponse
from django.views import View

from recipes.models.Msg_Tchat import Msg_Tchat


class RecipeListJsonView(View):
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        result = Msg_Tchat.objects.all()
        return JsonResponse(
            [a.title for a in result],
            safe=False
        )