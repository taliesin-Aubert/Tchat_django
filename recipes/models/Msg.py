from django.db import models

class Msg(models.Model):
    message = models.Charfield(max_length = 300, null = True, blank = True, default = '')

    def __str__(self):
        return self.message