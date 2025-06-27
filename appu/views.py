from django.shortcuts import render, redirect
from appu.models import Profesor
from appu.forms import ProfesorForm
from appu.models import Materia
from appu.forms import MateriaForm
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
        form = ProfesorForm
    return render(request,'profesorNew.html',{'form':form})

def profesorShow(request):
        profesor = Profesor.objects.all()
        return render(request,'profesorShow.html',{'profesor':profesor})

def profesorEdit(request, idprofesor):
        profesor = Profesor.objects.get(idprofesor = idprofesor)
        return render(request,'profesorEdit.html',{'profesor':profesor})

def profesorUpdate(request, idprofesor):
    profesor = Profesor.objects.get(idprofesor=idprofesor)
    old_image_path = None
    if profesor.imagen: # Verifica si ya tiene una imagen asociada
        old_image_path = profesor.imagen.path
    if request.method == 'POST':
        form = ProfesorForm(request.POST, request.FILES, instance=profesor)
        if form.is_valid():
            if 'imagen' in request.FILES and old_image_path:
                if old_image_path != profesor.imagen.path and os.path.isfile(old_image_path):
                    os.remove(old_image_path)
            form.save()
            return redirect("/showprofesor")
    else:
        form = ProfesorForm(instance=profesor) 
    return render(request, 'profesorEdit.html', {'profesor': profesor})       

def profesorDestroy(request, idprofesor):
    profesor = Profesor.objects.get(idprofesor=idprofesor)
    profesor.delete()
    if profesor.imagen: 
        if os.path.isfile(profesor.imagen.path):
            os.remove(profesor.imagen.path) 
    return redirect("/showprofesor")
    
# MANEJO DE MATERIAS

def materiaNew(request):
    form = MateriaForm(request.POST)
    if form.is_valid():
        try:
            form.save()
            return redirect('/showmateria')
        except:
            pass
    else:
        form = MateriaForm
    return render(request,'materiaNew.html',{'form':form})

def materiaShow(request):
        materia = Materia.objects.all()
        return render(request,'materiaShow.html',{'materia':materia})

def materiaEdit(request, idmateria):
        materia = Materia.objects.get(idmateria = idmateria)
        return render(request,'materiaEdit.html',{'materia':materia})

def materiaUpdate(request, idmateria):
        materia = Materia.objects.get(idmateria = idmateria)
        form = MateriaForm(request.POST,intance=materia)
        if form.is_valid():
            form.save()
            return redirect("/showmateria")
        return render(request,'materiaEdit.html',{'materia':materia})

def materiaDestroy(request, idmateria):
        materia = Materia.objects.get(idmateria = idmateria)
        materia.delete()
        return redirect("/showmateria")


