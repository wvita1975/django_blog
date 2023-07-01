from django.db import models
from django.urls import reverse

# Create your models here. Toda tabla viene con una llave primaria (Primary Key)

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    author = models.ForeignKey(
        "auth.User", 
        on_delete=models.CASCADE, # on delete: si se elimina el author, se borra todo lo queéste incluyó
    )
    def __str__(self): # devuelve el nombre del post que colocamos
          return self.title
    
    def get_absolute_url(self):
        return reverse("post_detail_view", kwargs={"pk": self.pk}) # entre llaves = diccionario python /post_detal ya que la app se llama post
