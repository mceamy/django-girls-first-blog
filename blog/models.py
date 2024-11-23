from django.conf import settings
#importando la configuracion de settings.py
from django.db import models
#importa la database
from django.utils import timezone
# Averiguar que importa******!!!!

#DOCUMENTACION DE DJANGO
#class: palabra clave que define un objeto
#Post: nombre de nuestro modelo
#models.Models: significa que Post es un modelo de Django
#models.CharField: define un texto con un numero limitado de caracteres
#models.TextField: texto largo sin limite
#models.DateTimeField: fecha y hora
#models.ForeignKey: link con otro modelo

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

#metodoPublish
    def publish(self):
        self.published_date = timezone.now()
        self.save()
#Obtener un texto string con un titulo de Post
    def __str__(self):
        return self.title