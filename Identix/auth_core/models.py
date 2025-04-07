from django.db import models
# Create your models here.
from oauth2_provider.models import AbstractApplication
class Scope(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name
    
class CustomApplication(AbstractApplication):
    scopes = models.ManyToManyField(Scope, blank=True)
    
    def __str__(self):
        return f'{self.id} - {self.name}'
