from django.shortcuts import render, redirect
from appu.models import Profesor
from appu.forms import ProfesorForm

# Create your views here.
def inicio(request):
    return render(request,'inicio.html',{})

def menu(request):
    return render(request,'menu.html',{}) 

# Manejo de profesores

def profesorNew(request):
    form = ProfesorForm(request.POST)
    if form.is_valid():
        try:
            form.save()
            return redirect('/showprofesor')
        except:
            pass
    else:
        form = ProfesorForm
    return render(request,'profesorNew.html',{'form':form})

def profesorShow(request):
        profesor = Profesor.objects.all()
        return render(request,'profesorShow.html',{'profesor':profesor})

def profesorEdit(request, idProfesor):
        profesor = Profesor.objects.get(idProfesor = idProfesor)
        return render(request,'profesorEdit.html',{'profesor':profesor})

def profesorUpdate(request, idProfesor):
        profesor = Profesor.objects.get(idProfesor = idProfesor)
        form = ProfesorForm(request.POST,intance=profesor)
        if form.is_valid():
            form.save()
            return redirect("/showprofesor")
        return render(request,'profesorEdit.html',{'profesor':profesor})

def profesorDestroy(request, idProfesor):
        profesor = Profesor.objects.get(idProfesor = idProfesor)
        profesor.delete()
        return redirect("/showprofesor")                           