from django import forms
from appu.models import Profesor
from appu.models import Materia

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = '__all__' # O la lista específica de campos que queremos usar

        # Usamos este widget para dar al usuario una ayuda al ingresar la fecha
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'especialidad': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'fecha_ingreso': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}), # ¡Aquí está la clave!
            
        }

class MateriaForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = '__all__' # O la lista específica de campos que queremos usar
