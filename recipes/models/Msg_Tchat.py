from django.db import models

from recipes.models.user import User
from recipes.models.Msg import Msg

class msg_Tchat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user?")
    msg = models.ForeignKey(Msg, on_delete=models.CASCADE, related_name="...")
    
    def __str__(self):
        return f"{self.user} / {self.msg}"
