from django.contrib import admin

from recipes.models.user import User
from recipes.models.Msg import Msg
from recipes.models.Msg_Tchat import Msg_Tchat

admin.site.register(User)
admin.site.register(Msg)
admin.site.register(Msg_Tchat)