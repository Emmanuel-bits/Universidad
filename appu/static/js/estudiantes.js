// Función para mostrar imagen en el modal
function showImage(imageUrl, nombre) {
    document.getElementById('modalImage').src = imageUrl;
    document.getElementById('imageModalLabel').textContent = nombre;
}

// Funciones para el formulario de nuevo/editar estudiante (con mejoras de UX)
function setupImagePreview() {
    const imagenInput = document.getElementById('id_imagen');
    const imagePreview = document.getElementById('imagePreview');

    if (imagenInput && imagePreview) {
        imagenInput.addEventListener('change', function(event) {
            const file = event.target.files[0];
            // Asume que el error estará después del input o en un elemento hermano
            const errorContainer = imagenInput.nextElementSibling; 

            if (!file) { // Si no se selecciona ningún archivo, limpiar errores y salir
                if (errorContainer && errorContainer.classList.contains('invalid-feedback')) {
                    errorContainer.textContent = '';
                }
                imagePreview.src = imagePreview.dataset.defaultSrc || '/static/images/default-avatar.png'; // Restaura la imagen por defecto
                imagenInput.classList.remove('is-invalid');
                return;
            }

            let errorMessage = '';

            // Validación básica del tipo de archivo
            if (!file.type.match('image/jpeg|image/png|image/gif')) {
                errorMessage = 'Por favor, seleccione un archivo de imagen válido (JPEG, PNG, GIF).';
            }
            // Validación del tamaño (ejemplo: máximo 2MB)
            else if (file.size > 2 * 1024 * 1024) {
                errorMessage = 'La imagen es demasiado grande. Tamaño máximo permitido: 2MB.';
            }

            if (errorMessage) {
                // Mostrar error visualmente
                imagenInput.classList.add('is-invalid');
                if (errorContainer && errorContainer.classList.contains('invalid-feedback')) {
                    errorContainer.textContent = errorMessage;
                } else {
                    // Si no hay un elemento invalid-feedback, crea uno.
                    const newError = document.createElement('div');
                    newError.className = 'invalid-feedback d-block';
                    newError.textContent = errorMessage;
                    imagenInput.parentNode.insertBefore(newError, imagenInput.nextSibling);
                }
                // No mostrar vista previa si hay error
                imagePreview.src = imagePreview.dataset.defaultSrc || '/static/images/default-avatar.png';
                imagenInput.value = ''; // Limpiar el input para permitir al usuario seleccionar de nuevo
            } else {
                // Limpiar errores si el archivo es válido
                imagenInput.classList.remove('is-invalid');
                if (errorContainer && errorContainer.classList.contains('invalid-feedback')) {
                    errorContainer.textContent = '';
                }

                // Mostrar vista previa
                const reader = new FileReader();
                reader.onload = function(e) {
                    imagePreview.src = e.target.result;
                }
                reader.readAsDataURL(file);
            }
        });

        // Almacena la URL por defecto para restaurar si se cancela o hay error
        if (!imagePreview.dataset.defaultSrc) {
            imagePreview.dataset.defaultSrc = imagePreview.src;
        }
    }
}

function setupFormValidation() {
    const form = document.querySelector('.post-form');
    if (form) {
        form.addEventListener('submit', function(event) {
            let isValid = true;

            // Función auxiliar para mostrar/limpiar errores de campo
            function setFieldError(elementId, message) {
                const element = document.getElementById(elementId);
                if (!element) return; // Asegúrate de que el elemento exista

                let errorDiv = element.nextElementSibling; // Busca el div de feedback

                // Crea el div si no existe o si no es el correcto
                if (!errorDiv || !errorDiv.classList.contains('invalid-feedback')) {
                    errorDiv = document.createElement('div');
                    errorDiv.className = 'invalid-feedback'; // Se hará 'd-block' por Bootstrap
                    element.parentNode.insertBefore(errorDiv, element.nextSibling);
                }

                if (message) {
                    errorDiv.textContent = message;
                    element.classList.add('is-invalid');
                    errorDiv.classList.add('d-block'); // Asegura que se muestre
                } else {
                    errorDiv.textContent = '';
                    element.classList.remove('is-invalid');
                    errorDiv.classList.remove('d-block');
                }
            }
            
            // Limpiar errores previos de validación JS
            setFieldError('id_telefono', '');
            setFieldError('id_email', '');
            setFieldError('id_fecha_nac', '');
            setFieldError('id_fecha_ing', '');


            // Validación de teléfono (solo números)
            const telefonoInput = document.getElementById('id_telefono');
            if (telefonoInput) {
                const telefono = telefonoInput.value;
                if (telefono && !/^\d+$/.test(telefono)) {
                    setFieldError('id_telefono', 'El teléfono debe contener solo números.');
                    isValid = false;
                }
            }

            // Validación de email (formato básico)
            const emailInput = document.getElementById('id_email');
            if (emailInput) {
                const email = emailInput.value;
                if (email && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
                    setFieldError('id_email', 'Por favor ingrese un email válido.');
                    isValid = false;
                }
            }

            // Validación de fecha de nacimiento (no futura)
            const fechaNacimientoInput = document.getElementById('id_fecha_nac');
            if (fechaNacimientoInput) {
                const fechaNacimiento = fechaNacimientoInput.value;
                if (fechaNacimiento) {
                    const hoy = new Date();
                    hoy.setHours(0,0,0,0); 
                    const fechaNacimientoDate = new Date(fechaNacimiento);
                    fechaNacimientoDate.setHours(0,0,0,0); 

                    if (fechaNacimientoDate > hoy) {
                        setFieldError('id_fecha_nac', 'La fecha de nacimiento no puede ser futura.');
                        isValid = false;
                    }
                }
            }

            // Validación de fecha de ingreso (no futura)
            const fechaIngresoInput = document.getElementById('id_fecha_ing');
            if (fechaIngresoInput) {
                const fechaIngreso = fechaIngresoInput.value;
                if (fechaIngreso) {
                    const hoy = new Date();
                    hoy.setHours(0,0,0,0); 
                    const fechaIngresoDate = new Date(fechaIngreso);
                    fechaIngresoDate.setHours(0,0,0,0); 

                    if (fechaIngresoDate > hoy) {
                        setFieldError('id_fecha_ing', 'La fecha de ingreso no puede ser futura.');
                        isValid = false;
                    }
                }
            }

            // Validación de Bootstrap HTML5
            if (!form.checkValidity()) {
                isValid = false;
            }

            if (!isValid) {
                event.preventDefault(); 
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        });
    }
}

// 4. Manejo de la modal de eliminación (NUEVO)
document.addEventListener('DOMContentLoaded', function() {
    const confirmDeleteModal = document.getElementById('confirmDeleteEstudianteModal'); // Usar ID del modal de estudiante
    if (confirmDeleteModal) {
        const confirmDeleteButton = document.getElementById('confirmDeleteEstudianteButton'); // Botón de eliminar dentro del modal
        
        confirmDeleteModal.addEventListener('show.bs.modal', function(event) {
            const button = event.relatedTarget; // El botón de la tabla que activó el modal
            const estudianteId = button.getAttribute('data-estudiante-id'); // Obtener el ID del estudiante

            if (confirmDeleteButton && estudianteId) {
                confirmDeleteButton.href = `/deleteestudiante/${estudianteId}/`; // Ajustar la URL de eliminación
            }
        });
    }
});


// 5. Funcionalidad de búsqueda en la tabla de estudiantes (NUEVO)
document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('searchInputEstudiantes'); // Usar ID del buscador de estudiante
    const estudiantesTable = document.getElementById('estudiantesTable'); // ID de la tabla de estudiantes

    if (searchInput && estudiantesTable) {
        searchInput.addEventListener('keyup', function() {
            const searchText = this.value.toLowerCase();
            const rows = estudiantesTable.getElementsByTagName('tbody')[0].getElementsByTagName('tr');

            for (let i = 0; i < rows.length; i++) {
                let row = rows[i];
                // Celdas a buscar (ajusta los índices según las columnas de tu tabla de estudiante)
                let cellsToSearch = [
                    row.cells[1], // Identificación
                    row.cells[2], // Nombre
                    row.cells[3], // Apellido
                    row.cells[4], // Dirección
                    row.cells[5], // Teléfono
                    row.cells[6], // Email
                    row.cells[7], // Estado
                    row.cells[8], // Fecha_nac
                    row.cells[9], // Fecha_ing
                ];
                let found = false;

                for (let j = 0; j < cellsToSearch.length; j++) {
                    const cell = cellsToSearch[j];
                    if (cell) { // Asegurarse de que la celda existe
                        let cellText = cell.textContent.toLowerCase();
                        if (cellText.includes(searchText)) {
                            found = true;
                            break;
                        }
                    }
                }

                if (found) {
                    row.style.display = ''; // Muestra la fila
                } else {
                    row.style.display = 'none'; // Oculta la fila
                }
            }
        });
    }
});


// Inicialización cuando el DOM está listo
document.addEventListener('DOMContentLoaded', function() {
    console.log('Script de estudiantes cargado correctamente - Versión con búsqueda y modal de eliminación');
    
    // Configurar vista previa de imagen (para formulario de nuevo/editar estudiante)
    setupImagePreview();
    
    // Configurar validaciones del formulario
    setupFormValidation();

    // Las funcionalidades de modal de eliminación y búsqueda ya están envueltas en sus propios DOMContentLoaded
    // para mayor modularidad, pero también se podrían llamar directamente aquí si prefieres un único listener.
});
