from django.db import models

class User(models.Model):
    pseudo = models.Charfield(max_length = 20, null = True, blank = True, default = '')