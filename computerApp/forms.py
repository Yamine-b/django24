from cgi import test
from computerApp.models import Machine
from django import forms
from django.core.exceptions import ValidationError

class AddMachineForm(forms.Form):
    nom = forms.CharField(required=True, label='Nom de la machine')
    TYPE = (
        ('PC', ('PC - Run windows')),
        ('Mac', ('Mac - Run MacOS')),
        ('Switch',('Switch - To maintains and connect servers')),
        ('Router', ('Router - Connect different network')),
        ('Server', ('Server - To stock data or services')),
    )
    mach = forms.ChoiceField(required=True,widget=forms.RadioSelect, choices=TYPE)

    def clean_nom(self):
        data = self.cleaned_data["nom"]
        if len(data) > 25:
            raise ValidationError("Erreur de format pour le champ nom")
        return data
    
    def clean_type(self):
        data = self.cleaned_data["mach"]
        return data