from django.shortcuts import render, redirect
from appu.models import Profesor
from appu.forms import ProfesorForm
from appu.models import Materia
from appu.forms import MateriaForm
import os # Importamos el módulo 'os'

# ... (El resto de tus vistas, como inicio, menu, profesorNew, profesorShow, profesorEdit, etc. permanecen igual) ...

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

# ... (El resto de tus vistas, incluyendo profesorDestroy modificado, y las vistas de Materia permanecen igual) ...