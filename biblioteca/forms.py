
from django import forms
from .models import Libro

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = '__all__'

    def clean_titulo(self):
        titulo = self.cleaned_data['titulo']
        if "django" not in titulo.lower():
            raise forms.ValidationError("El título debe contener la palabra 'django'.")
        return titulo
