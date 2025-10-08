from django.db import models

# Create your models here.
class Dojos(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=20)
    
    
class Ninjas(models.Model):
    first_name = models.CharField(255)
    last_name = models.CharField(255)
    dojo = models.ForeignKey(Dojos, related_name='dojos', on_delete=models.CASCADE)
    
    
def get_all_dojos():
    return Dojos.objects.all()

