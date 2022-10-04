from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class ColaboradorModel(models.Model):
    user = models.OneToOneField(User, verbose_name="usuario", related_name="colaborador", on_delete=models.CASCADE)

    def __str__(self):
        datos = str(self.user) + " " + self.user.first_name + " " + self.user.last_name
        return datos
