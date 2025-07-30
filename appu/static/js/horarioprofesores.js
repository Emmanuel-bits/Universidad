document.addEventListener('DOMContentLoaded', function() {
    console.log('Script de horarios de profesores cargado correctamente');

    // 1. Manejo de la modal de eliminación
    const confirmDeleteHorarioProfesorModal = document.getElementById('confirmDeleteHorarioProfesorModal');
    if (confirmDeleteHorarioProfesorModal) {
        const confirmDeleteHorarioProfesorButton = document.getElementById('confirmDeleteHorarioProfesorButton');
        confirmDeleteHorarioProfesorModal.addEventListener('show.bs.modal', function(event) {
            const button = event.relatedTarget; // Botón que disparó el modal
            const horarioProfesorId = button.getAttribute('data-horarioprofesor-id');
            if (confirmDeleteHorarioProfesorButton && horarioProfesorId) {
                // Actualiza el href del botón de eliminación en la modal
                confirmDeleteHorarioProfesorButton.href = `/deletehorarioprofesor/${horarioProfesorId}`;
            }
        });
    }

    // 2. Funcionalidad de búsqueda en la tabla de horarios de profesores
    const searchInput = document.getElementById('searchInputHorarioProfesores');
    const horariosProfesoresTable = document.getElementById('horarioProfesoresTable');

    if (searchInput && horariosProfesoresTable) {
        searchInput.addEventListener('keyup', function() {
            const searchText = this.value.toLowerCase();
            const rows = horariosProfesoresTable.getElementsByTagName('tbody')[0].getElementsByTagName('tr');
            const cellsToSearch = [0, 1, 2, 3, 4, 5, 6];

            for (let i = 0; i < rows.length; i++) {
                let row = rows[i];
                let cells = row.getElementsByTagName('td');
                let found = false;

                // Itera sobre las celdas relevantes para la búsqueda
                for (let j = 0; j < cellsToSearch.length; j++) {
                    const cellIndex = cellsToSearch[j];
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

});
