from django.db import models
from datetime import datetime

# Create your models here.
class Machine(models.Model):
    id = models.AutoField(
        primary_key=True,
        editable=False)
    nom= models.CharField(
        max_length=200)
    
    def __str__(self):
        return str(self.id) + " -> " + self.nom

    def get_name(self):
        return str(self.id) + " " + self.nom

    TYPE = (
        ('PC', ('PC - Run windows')),
        ('Mac', ('Mac - Run MacOS')),
        ('Serveur',('Switch - To maintains and connect servers')),
    )
    maintenanceDate= models.DateField(default= datetime.now())
    mach= models.CharField(max_length=32, choices=TYPE, default='PC')


