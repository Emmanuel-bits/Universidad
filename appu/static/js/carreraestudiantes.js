// Este script maneja la interactividad del lado del cliente para la tabla "Estudiantes en Carrera".

document.addEventListener('DOMContentLoaded', function() {
    console.log('Script de carreraestudiantes cargado correctamente');

    // 1. Funcionalidad de búsqueda en la tabla de estudiantes en carrera
    const searchInput = document.getElementById('searchInputCarreraEstudiantes');
    const table = document.getElementById('carreraEstudiantesTable');

    if (searchInput && table) {
        searchInput.addEventListener('keyup', function() {
            const searchText = this.value.toLowerCase();
            const rows = table.getElementsByTagName('tbody')[0].getElementsByTagName('tr');

            for (let i = 0; i < rows.length; i++) {
                let row = rows[i];
                let cells = row.getElementsByTagName('td');
                let found = false;

                const cellsToSearch = [0, 1, 2]; // Índices de las columnas a incluir en la búsqueda

                for (let j = 0; j < cellsToSearch.length; j++) {
                    let cellIndex = cellsToSearch[j];
                    if (cells[cellIndex]) { // Asegura que la celda exista
                        let cellText = cells[cellIndex].textContent.toLowerCase();
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

    // 2. Manejo de la modal de eliminación
    const confirmDeleteModal = document.getElementById('confirmDeleteCarreraEstudianteModal');
    if (confirmDeleteModal) {
        const confirmDeleteButton = document.getElementById('confirmDeleteCarreraEstudianteButton');
        confirmDeleteModal.addEventListener('show.bs.modal', function(event) {
            // Botón que disparó el modal
            const button = event.relatedTarget;
            // Obtiene el ID del estudiante en carrera del atributo data-carreraestudiante-id
            const carreraEstudianteId = button.getAttribute('data-carreraestudiante-id');

            if (confirmDeleteButton && carreraEstudianteId) {
                // Actualiza el atributo href del botón de confirmación en la modal
                confirmDeleteButton.href = `/deletecarreraestudiante/${carreraEstudianteId}`;
            }
        });
    }
});
