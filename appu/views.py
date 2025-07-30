from django.shortcuts import render, redirect
from django.core.paginator import Paginator # Importar la clase Paginator
from appu.models import Profesor
from appu.forms import ProfesorForm
from appu.models import Estudiante
from appu.forms import EstudianteForm
from appu.models import Materia
from appu.forms import MateriaForm
from appu.models import Carrera
from appu.forms import CarreraForm
from appu.models import Aula
from appu.forms import AulaForm
from appu.models import HorarioEstudiante
from appu.forms import HorarioEstudianteForm
from appu.models import HorarioProfesor
from appu.forms import HorarioProfesorForm
from appu.models import CarreraEstudiante
from appu.forms import CarreraEstudianteForm
from appu.models import MateriaProfesor
from appu.forms import MateriaProfesorForm
from appu.models import Nota
from appu.forms import NotaForm 
import os

# Create your views here.
def inicio(request):
    return render(request,'inicio.html',{})

def menu(request):
    return render(request,'menu.html',{}) 

# Manejo de profesores

def profesorNew(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/showprofesor')
    else:
        form = ProfesorForm()
    return render(request,'profesorNew.html',{'form':form})

def profesorShow(request):
    profesores_list = Profesor.objects.all() # Obtener todos los objetos
    paginator = Paginator(profesores_list, 5) # Mostrar 5 profesores por página
    page_number = request.GET.get('page') # Obtener el número de página de la URL
    page_obj = paginator.get_page(page_number) # Obtener el objeto de página
    return render(request,'profesorShow.html',{'profesor':page_obj}) # Pasar page_obj al template

def profesorEdit(request, idprofesor):
    profesor = Profesor.objects.get(idprofesor = idprofesor)
    form = ProfesorForm(instance=profesor) # Pasar form para pre-llenado
    return render(request,'profesorEdit.html',{'profesor':profesor, 'form':form})

def profesorUpdate(request, idprofesor):
    profesor = Profesor.objects.get(idprofesor=idprofesor)
    old_image_path = None
    if profesor.imagen: # Verifica si ya tiene una imagen asociada
        old_image_path = profesor.imagen.path
    if request.method == 'POST':
        form = ProfesorForm(request.POST, request.FILES, instance=profesor)
        if form.is_valid():
            if 'imagen' in request.FILES: # Verifica si se envió un nuevo archivo de imagen
                if old_image_path and os.path.isfile(old_image_path) and old_image_path != profesor.imagen.path:
                    os.remove(old_image_path)
            form.save()
            return redirect("/showprofesor")
        else:
            print("Errores de validación en Profesor Update:", form.errors)
    else:
        form = ProfesorForm(instance=profesor) 
    return render(request, 'profesorEdit.html', {'profesor': profesor, 'form': form})      

def profesorDestroy(request, idprofesor):
    profesor = Profesor.objects.get(idprofesor=idprofesor)
    profesor.delete()
    if profesor.imagen: 
        if os.path.isfile(profesor.imagen.path):
            os.remove(profesor.imagen.path) 
    return redirect("/showprofesor")

# MANEJO DE ESTUDIANTES

def estudianteNew(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/showestudiante')
    else:
        form = EstudianteForm() 
    return render(request,'estudianteNew.html',{'form':form})

def estudianteShow(request):
    estudiantes_list = Estudiante.objects.all() # Obtener todos los objetos
    paginator = Paginator(estudiantes_list, 5) # Mostrar 5 estudiantes por página
    page_number = request.GET.get('page') # Obtener el número de página de la URL
    page_obj = paginator.get_page(page_number) # Obtener el objeto de página
    return render(request,'estudianteShow.html',{'estudiante':page_obj}) # Pasar page_obj al template

def estudianteEdit(request, idestudiante):
    estudiante = Estudiante.objects.get(idestudiante = idestudiante)
    form = EstudianteForm(instance=estudiante) # Pasar form para pre-llenado
    return render(request,'estudianteEdit.html',{'estudiante':estudiante, 'form':form})

def estudianteUpdate(request, idestudiante):
    estudiante = Estudiante.objects.get(idestudiante=idestudiante)
    old_image_path = None
    if estudiante.imagen: # Verifica si ya tiene una imagen asociada
        old_image_path = estudiante.imagen.path
    if request.method == 'POST':
        form = EstudianteForm(request.POST, request.FILES, instance=estudiante)
        if form.is_valid():
            # Si se sube una nueva imagen y había una antigua, la elimina
            if 'imagen' in request.FILES:
                # Comprueba que la nueva imagen no sea la misma que la antigua
                if old_image_path and os.path.isfile(old_image_path) and old_image_path != estudiante.imagen.path:
                    os.remove(old_image_path)
            form.save()
            return redirect("/showestudiante")
        else:
            print("Errores de validación en Estudiante Update:", form.errors)
    else:
        form = EstudianteForm(instance=estudiante) 
    return render(request, 'estudianteEdit.html', {'estudiante': estudiante, 'form': form})

def estudianteDestroy(request, idestudiante):
    estudiante = Estudiante.objects.get(idestudiante=idestudiante)
    estudiante.delete()
    if estudiante.imagen: 
        if os.path.isfile(estudiante.imagen.path):
            os.remove(estudiante.imagen.path) 
    return redirect("/showestudiante")


# MANEJO DE CARRERAS

def carreraNew(request):
    if request.method == 'POST':
        form = CarreraForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/showcarrera')
            except Exception as e:
                print(f"Error al guardar carrera: {e}")
                print("Errores del formulario de Carrera:", form.errors)
    else:
        form = CarreraForm()
    return render(request, 'carreraNew.html', {'form': form})

def carreraShow(request):
    carreras_list = Carrera.objects.all() # Obtener todos los objetos
    paginator = Paginator(carreras_list, 5) # Mostrar 5 carreras por página
    page_number = request.GET.get('page') # Obtener el número de página de la URL
    page_obj = paginator.get_page(page_number) # Obtener el objeto de página
    return render(request, 'carreraShow.html', {'carrera': page_obj}) # Pasar page_obj al template

def carreraEdit(request, idcarrera):
    carrera = Carrera.objects.get(idcarrera=idcarrera)
    form = CarreraForm(instance=carrera) 
    return render(request, 'carreraEdit.html', {'carrera': carrera, 'form': form})

def carreraUpdate(request, idcarrera):
    carrera = Carrera.objects.get(idcarrera=idcarrera)
    if request.method == 'POST':
        form = CarreraForm(request.POST, instance=carrera)
        if form.is_valid():
            form.save()
            return redirect('/showcarrera')
        else:
            print("Errores de validación en Carrera Update:", form.errors)
    else:
        form = CarreraForm(instance=carrera)
    return render(request, 'carreraEdit.html', {'carrera': carrera, 'form': form})

def carreraDestroy(request, idcarrera):
    carrera = Carrera.objects.get(idcarrera=idcarrera)
    carrera.delete()
    return redirect('/showcarrera')


# MANEJO DE MATERIAS

def materiaNew(request):
    if request.method == 'POST':
        form = MateriaForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/showmateria')
            except Exception as e:
                print(f"Error al guardar materia: {e}")
                print("Errores del formulario de Materia:", form.errors)
    else:
        form = MateriaForm()
    return render(request,'materiaNew.html',{'form':form})

def materiaShow(request):
    materias_list = Materia.objects.all() # Obtener todos los objetos
    paginator = Paginator(materias_list, 5) # Mostrar 5 materias por página
    page_number = request.GET.get('page') # Obtener el número de página de la URL
    page_obj = paginator.get_page(page_number) # Obtener el objeto de página
    return render(request,'materiaShow.html',{'materia':page_obj}) # Pasar page_obj al template

def materiaEdit(request, idmateria):
    materia = Materia.objects.get(idmateria=idmateria)
    form = MateriaForm(instance=materia)
    return render(request,'materiaEdit.html',{'materia':materia, 'form': form})

def materiaUpdate(request, idmateria):
    materia = Materia.objects.get(idmateria=idmateria)
    if request.method == 'POST':
        form = MateriaForm(request.POST, instance=materia)
        if form.is_valid():
            form.save()
            return redirect("/showmateria")
        else:
            return render(request,'materiaEdit.html',{'materia':materia, 'form': form})
    else:
        form = MateriaForm(instance=materia)
    return render(request,'materiaEdit.html',{'materia':materia, 'form': form})

def materiaDestroy(request, idmateria):
    materia = Materia.objects.get(idmateria=idmateria)
    materia.delete()
    return redirect("/showmateria")


# MANEJO DE AULAS

def aulaNew(request):
    if request.method == 'POST':
        form = AulaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/showaula')
    else:
        form = AulaForm()
    return render(request, 'aulaNew.html', {'form': form})

def aulaShow(request):
    aulas_list = Aula.objects.all() # Obtener todos los objetos
    paginator = Paginator(aulas_list, 5) # Mostrar 5 aulas por página
    page_number = request.GET.get('page') # Obtener el número de página de la URL
    page_obj = paginator.get_page(page_number) # Obtener el objeto de página
    return render(request, 'aulaShow.html', {'aula': page_obj}) # Pasar page_obj al template

def aulaEdit(request, idaula):
    aula = Aula.objects.get(idaula=idaula)
    form = AulaForm(instance=aula)
    return render(request, 'aulaEdit.html', {'aula': aula, 'form': form})

def aulaUpdate(request, idaula):
    aula = Aula.objects.get(idaula=idaula)
    if request.method == 'POST':
        form = AulaForm(request.POST, instance=aula)
        if form.is_valid():
            form.save()
            return redirect("/showaula")
        else:
            print("Errores de validación en Aula Update:", form.errors)
    else:
        form = AulaForm(instance=aula)
    return render(request, 'aulaEdit.html', {'aula': aula, 'form': form})

def aulaDestroy(request, idaula):
    aula = Aula.objects.get(idaula=idaula)
    aula.delete()
    return redirect("/showaula")


# MANEJO DE HORARIOS PARA ESTUDIANTES

def horarioestudianteNew(request):
    if request.method == 'POST':
        form = HorarioEstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/showhorarioestudiante')
        else:
            print("Formulario de HorarioEstudiante no válido:", form.errors)
    else:
        form = HorarioEstudianteForm()
    return render(request, 'horarioestudianteNew.html', {'form': form})

def horarioestudianteShow(request):
    horarioestudiantes_list = HorarioEstudiante.objects.all() # Obtener todos los objetos
    paginator = Paginator(horarioestudiantes_list, 5) # Mostrar 5 horarios por página
    page_number = request.GET.get('page') # Obtener el número de página de la URL
    page_obj = paginator.get_page(page_number) # Obtener el objeto de página
    return render(request, 'horarioestudianteShow.html', {'horarioestudiante': page_obj}) # Pasar page_obj al template

def horarioestudianteEdit(request, id):
    horarioestudiante = HorarioEstudiante.objects.get(id=id)
    form = HorarioEstudianteForm(instance=horarioestudiante)
    return render(request, 'horarioestudianteEdit.html', {'horarioestudiante': horarioestudiante, 'form': form})

def horarioestudianteUpdate(request, id):
    horarioestudiante = HorarioEstudiante.objects.get(id=id)
    if request.method == 'POST':
        form = HorarioEstudianteForm(request.POST, instance=horarioestudiante)
        if form.is_valid():
            form.save()
            return redirect('/showhorarioestudiante')
        else:
            print("Errores de validación en HorarioEstudiante Update:", form.errors)
            return render(request, 'horarioestudianteEdit.html', {'horarioestudiante': horarioestudiante, 'form': form})
    else:
        form = HorarioEstudianteForm(instance=horarioestudiante)
    return render(request, 'horarioestudianteEdit.html', {'horarioestudiante': horarioestudiante, 'form': form})

def horarioestudianteDestroy(request, id):
    horarioestudiante = HorarioEstudiante.objects.get(id=id)
    horarioestudiante.delete()
    return redirect('/showhorarioestudiante')

# MANEJO DE HORARIOS PARA PROFESORES

def horarioprofesorNew(request):
    if request.method == 'POST':
        form = HorarioProfesorForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/showhorarioprofesor')
            except Exception as e:
                print(f"Error al guardar horario de profesor: {e}")
                print("Errores del formulario de HorarioProfesor:", form.errors)
        else:
            print("Formulario de HorarioProfesor no válido:", form.errors)
    else:
        form = HorarioProfesorForm()
    return render(request, 'horarioprofesorNew.html', {'form': form})

def horarioprofesorShow(request):
    horarioprofesor_list = HorarioProfesor.objects.all() # Obtener todos los objetos
    paginator = Paginator(horarioprofesor_list, 5) # Mostrar 5 horarios por página
    page_number = request.GET.get('page') # Obtener el número de página de la URL
    page_obj = paginator.get_page(page_number) # Obtener el objeto de página
    return render(request, 'horarioprofesorShow.html', {'horarioprofesor': page_obj}) # Pasar page_obj al template

def horarioprofesorEdit(request, id):
    horarioprofesor = HorarioProfesor.objects.get(id=id)
    form = HorarioProfesorForm(instance=horarioprofesor)
    return render(request, 'horarioprofesorEdit.html', {'horarioprofesor': horarioprofesor, 'form': form})

def horarioprofesorUpdate(request, id):
    horarioprofesor = HorarioProfesor.objects.get(id=id)
    if request.method == 'POST':
        form = HorarioProfesorForm(request.POST, instance=horarioprofesor)
        if form.is_valid():
            form.save()
            return redirect("/showhorarioprofesor")
        else:
            print("Errores de validación en HorarioProfesor Update:", form.errors)
            return render(request, 'horarioprofesorEdit.html', {'horarioprofesor': horarioprofesor, 'form': form})
    else:
        form = HorarioProfesorForm(instance=horarioprofesor)
    return render(request, 'horarioprofesorEdit.html', {'horarioprofesor': horarioprofesor, 'form': form})

def horarioprofesorDestroy(request, id):
    horarioprofesor = HorarioProfesor.objects.get(id=id)
    horarioprofesor.delete()
    return redirect("/showhorarioprofesor")

# MANEJO DE ESTUDIANTES EN CARRERAS

def carreraestudianteNew(request):
    if request.method == 'POST':
        form = CarreraEstudianteForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/showcarreraestudiante')
            except Exception as e:
                print(f"Error al guardar estudiante en carrera: {e}")
                print("Errores del formulario de Estudiante en Carrera:", form.errors)
    else:
        form = CarreraEstudianteForm()
    return render(request, 'carreraestudianteNew.html', {'form': form})

def carreraestudianteShow(request):
    carreraestudiante_list = CarreraEstudiante.objects.all() # Obtener todos los objetos
    paginator = Paginator(carreraestudiante_list, 5) # Mostrar 5 registros por página
    page_number = request.GET.get('page') # Obtener el número de página de la URL
    page_obj = paginator.get_page(page_number) # Obtener el objeto de página
    return render(request, 'carreraestudianteShow.html', {'carreraestudiante': page_obj}) # Pasar page_obj al template

def carreraestudianteEdit(request, id):
    carreraestudiante = CarreraEstudiante.objects.get(id=id)
    form = CarreraEstudianteForm(instance=carreraestudiante) # Para pre-llenar el formulario
    return render(request, 'carreraestudianteEdit.html', {'carreraestudiante': carreraestudiante, 'form': form})

def carreraestudianteUpdate(request, id):
    carreraestudiante = CarreraEstudiante.objects.get(id=id)
    if request.method == 'POST':
        form = CarreraEstudianteForm(request.POST, instance=carreraestudiante)
        if form.is_valid():
            form.save()
            return redirect("/showcarreraestudiante")
        else:
            print("Errores de validación en CarreraEstudiante Update:", form.errors)
            return render(request, 'carreraestudianteEdit.html', {'carreraestudiante': carreraestudiante, 'form': form})
    else: 
        form = CarreraEstudianteForm(instance=carreraestudiante)
    return render(request, 'carreraestudianteEdit.html', {'carreraestudiante': carreraestudiante, 'form': form})

def carreraestudianteDestroy(request, id):
    carreraestudiante = CarreraEstudiante.objects.get(id=id)
    carreraestudiante.delete()
    return redirect("/showcarreraestudiante")

# MANEJO DE MATERIAS PROFESOR

def materiaprofesorNew(request):
    if request.method == 'POST':
        form = MateriaProfesorForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/showmateriaprofesor')
            except Exception as e:
                print(f"Error al guardar asignación Materia-Profesor: {e}")
                print("Errores del formulario de Asignación Materia-Profesor:", form.errors)
    else:
        form = MateriaProfesorForm()
    return render(request,'materiaprofesorNew.html',{'form':form})

def materiaprofesorShow(request):
    materiaprofesor_list = MateriaProfesor.objects.all() # Obtener todos los objetos
    paginator = Paginator(materiaprofesor_list, 5) # Mostrar 5 registros por página
    page_number = request.GET.get('page') # Obtener el número de página de la URL
    page_obj = paginator.get_page(page_number) # Obtener el objeto de página
    return render(request,'materiaprofesorShow.html',{'materiaprofesor':page_obj}) # Pasar page_obj al template

def materiaprofesorEdit(request, id):
    materiaprofesor = MateriaProfesor.objects.get(id=id)
    form = MateriaProfesorForm(instance=materiaprofesor)
    return render(request,'materiaprofesorEdit.html',{'materiaprofesor':materiaprofesor, 'form': form})

def materiaprofesorUpdate(request, id):
    materiaprofesor = MateriaProfesor.objects.get(id=id)
    if request.method == 'POST':
        form = MateriaProfesorForm(request.POST, instance=materiaprofesor)
        if form.is_valid():
            form.save()
            return redirect("/showmateriaprofesor")
        else:
            print("Errores de validación en Asignación Materia-Profesor Update:", form.errors)
            return render(request,'materiaprofesorEdit.html',{'materiaprofesor':materiaprofesor, 'form': form})
    else:
        form = MateriaProfesorForm(instance=materiaprofesor)
    return render(request,'materiaprofesorEdit.html',{'materiaprofesor':materiaprofesor, 'form': form})

def materiaprofesorDestroy(request, id):
    materiaprofesor = MateriaProfesor.objects.get(id=id)
    materiaprofesor.delete()
    return redirect("/showmateriaprofesor")


# MANEJO DE NOTAS

def notaNew(request):
    if request.method == 'POST':
        form = NotaForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/shownota')
            except Exception as e:
                print(f"Error al guardar nota: {e}")
                print("Errores del formulario de Nota:", form.errors)
    else:
        form = NotaForm()
    return render(request,'notaNew.html',{'form':form})

def notaShow(request):
    nota_list = Nota.objects.all() # Obtener todos los objetos
    paginator = Paginator(nota_list, 5) # Mostrar 5 notas por página
    page_number = request.GET.get('page') # Obtener el número de página de la URL
    page_obj = paginator.get_page(page_number) # Obtener el objeto de página
    return render(request,'notaShow.html',{'nota':page_obj}) # Pasar page_obj al template

def notaEdit(request, id):
    nota = Nota.objects.get(id=id)
    form = NotaForm(instance=nota)
    return render(request,'notaEdit.html',{'nota':nota, 'form': form})

def notaUpdate(request, id):
    nota = Nota.objects.get(id=id)
    if request.method == 'POST':
        form = NotaForm(request.POST, instance=nota)
        if form.is_valid():
            form.save()
            return redirect("/shownota")
        else:
            print("Errores de validación en Nota Update:", form.errors)
            return render(request,'notaEdit.html',{'nota':nota, 'form': form})
    else:
        form = NotaForm(instance=nota)
    return render(request,'notaEdit.html',{'nota':nota, 'form': form})

def notaDestroy(request, id):
    nota = Nota.objects.get(id=id)
    nota.delete()
    return redirect("/shownota")
