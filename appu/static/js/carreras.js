document.addEventListener('DOMContentLoaded', function() {
    console.log('Script de carreras cargado correctamente');


    // 1. Manejo de la modal de eliminación para Carreras
    const confirmDeleteCarreraModal = document.getElementById('confirmDeleteCarreraModal');
    if (confirmDeleteCarreraModal) {
        const confirmDeleteCarreraButton = document.getElementById('confirmDeleteCarreraButton');
        confirmDeleteCarreraModal.addEventListener('show.bs.modal', function(event) {
            // Botón que activó el modal (el botón de "Eliminar" de la fila)
            const button = event.relatedTarget; 
            // Obtener el ID de la carrera del atributo data-carrera-id
            const carreraId = button.getAttribute('data-carrera-id');
            
            if (confirmDeleteCarreraButton && carreraId) {
                // Actualizar el href del botón de confirmación en el modal
                confirmDeleteCarreraButton.href = `/deletecarrera/${carreraId}`;
            }
        });
    }

    // 2. Funcionalidad de búsqueda en la tabla de carreras
    const searchInputCarreras = document.getElementById('searchInputCarreras');
    const carrerasTable = document.getElementById('carrerasTable');

    if (searchInputCarreras && carrerasTable) {
        searchInputCarreras.addEventListener('keyup', function() {
            const searchText = this.value.toLowerCase(); // Texto de búsqueda en minúsculas
            // Obtener todas las filas del cuerpo de la tabla
            const rows = carrerasTable.getElementsByTagName('tbody')[0].getElementsByTagName('tr');

            for (let i = 0; i < rows.length; i++) {
                let row = rows[i];
                let cells = row.getElementsByTagName('td'); // Obtener todas las celdas de la fila
                let found = false; // Bandera para saber si se encontró el texto en la fila

                // Itera sobre las celdas de la fila (excluyendo la última que es la de "Acciones")
                // Ajusta el 'cells.length - 1' si la columna de acciones no es la última o si hay más columnas a ignorar
                for (let j = 0; j < cells.length - 1; j++) { 
                    let cellText = cells[j].textContent.toLowerCase(); // Texto de la celda en minúsculas
                    if (cellText.includes(searchText)) {
                        found = true; // Se encontró el texto
                        break; // Salir del bucle de celdas, ya que se encontró en esta fila
                    }
                }

                if (found) {
                    row.style.display = ''; // Muestra la fila si se encontró el texto
                } else {
                    row.style.display = 'none'; // Oculta la fila si no se encontró el texto
                }
            }
        });
    }

});
