from computerApp.models import Machine
from django import forms
from django.core.exceptions import ValidationError

class createMachineForm(forms.Form):
    nom = forms.CharField(label="Nom de la machine")
    def clean_nom(self):
        data = self.cleaned_data["nom"]
        if len(data) != 6:
            raise ValidationError(("Erreur de format pour le champ 'nom'"))
        return data