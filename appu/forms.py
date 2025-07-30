from django import forms
from appu.models import Profesor
from appu.models import Estudiante
from appu.models import Materia
from appu.models import Carrera
from appu.models import Aula
from appu.models import HorarioEstudiante
from appu.models import HorarioProfesor
from appu.models import CarreraEstudiante
from appu.models import MateriaProfesor
from appu.models import Nota                            

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

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = '__all__' # O la lista específica de campos que queremos usar

class MateriaForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = '__all__' # O la lista específica de campos que queremos usar

class CarreraForm(forms.ModelForm):
    class Meta:
        model = Carrera
        fields = '__all__' # O la lista específica de campos que queremos usar

class AulaForm(forms.ModelForm):
    class Meta:
        model = Aula
        fields = '__all__' # O la lista específica de campos que queremos usar


class HorarioEstudianteForm(forms.ModelForm):
    class Meta:
        model = HorarioEstudiante
        fields = '__all__'
        

class HorarioProfesorForm(forms.ModelForm):
    class Meta:
        model = HorarioProfesor
        fields = '__all__'
        

class NotaForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = '__all__'
        

class CarreraEstudianteForm(forms.ModelForm):
    class Meta:
        model = CarreraEstudiante
        fields = '__all__'
        

class MateriaProfesorForm(forms.ModelForm):
    class Meta:
        model = MateriaProfesor
        fields = '__all__'
        

