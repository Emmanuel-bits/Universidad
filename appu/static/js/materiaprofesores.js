document.addEventListener('DOMContentLoaded', function() {
    console.log('Script de materiaprofesores cargado correctamente.');

    // 1. Manejo de la modal de eliminación
    const confirmDeleteMateriaProfesorModal = document.getElementById('confirmDeleteMateriaProfesorModal');
    if (confirmDeleteMateriaProfesorModal) {
        const confirmDeleteMateriaProfesorButton = document.getElementById('confirmDeleteMateriaProfesorButton');
        confirmDeleteMateriaProfesorModal.addEventListener('show.bs.modal', function(event) {
            const button = event.relatedTarget; // Botón que activó el modal
            const materiaProfesorId = button.getAttribute('data-materiaprofesor-id'); // Obtener el ID del botón

            if (confirmDeleteMateriaProfesorButton && materiaProfesorId) {
                // Construir la URL de eliminación y asignarla al botón de confirmación
                confirmDeleteMateriaProfesorButton.href = `/deletemateriaprofesor/${materiaProfesorId}/`;
            }
        });
    }

    // 2. Funcionalidad de búsqueda en la tabla
    const searchInputMateriaProfesores = document.getElementById('searchInputMateriaProfesores');
    const materiaProfesoresTable = document.getElementById('materiaProfesoresTable');

    if (searchInputMateriaProfesores && materiaProfesoresTable) {
        searchInputMateriaProfesores.addEventListener('keyup', function() {
            const searchText = this.value.toLowerCase();
            const rows = materiaProfesoresTable.getElementsByTagName('tbody')[0].getElementsByTagName('tr');

            for (let i = 0; i < rows.length; i++) {
                let row = rows[i];
                // Las celdas a buscar son: ID Asignación, Profesor (nombre y apellido), Materia
                // Se excluye la última celda que es la de "Acciones"
                let cellsToSearch = [
                    row.cells[0], // ID Asignación
                    row.cells[1], // Profesor
                    row.cells[2]  // Materia
                ];
                let found = false;

                for (let j = 0; j < cellsToSearch.length; j++) {
                    let cellText = cellsToSearch[j].textContent.toLowerCase();
                    if (cellText.includes(searchText)) {
                        found = true;
                        break;
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
