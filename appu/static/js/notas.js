document.addEventListener('DOMContentLoaded', function() {
    console.log('Script de notas cargado correctamente');

    // 1. Manejo de la modal de eliminación para Notas
    const confirmDeleteNotaModal = document.getElementById('confirmDeleteNotaModal');
    if (confirmDeleteNotaModal) {
        const confirmDeleteNotaButton = document.getElementById('confirmDeleteNotaButton');
        confirmDeleteNotaModal.addEventListener('show.bs.modal', function(event) {
            // Botón que disparó el modal
            const button = event.relatedTarget;
            // Extraer el ID del registro de nota
            const notaId = button.getAttribute('data-nota-id');
            
            // Si el botón de confirmación y el ID existen, actualizar el href
            if (confirmDeleteNotaButton && notaId) {
                confirmDeleteNotaButton.href = `/deletenota/${notaId}/`;
            }
        });
    }

    // 2. Funcionalidad de búsqueda en la tabla de notas
    const searchInputNotas = document.getElementById('searchInputNotas');
    const notasTable = document.getElementById('notasTable');

    if (searchInputNotas && notasTable) {
        searchInputNotas.addEventListener('keyup', function() {
            const searchText = this.value.toLowerCase();
            const rows = notasTable.getElementsByTagName('tbody')[0].getElementsByTagName('tr');

            for (let i = 0; i < rows.length; i++) {
                let row = rows[i];
                // Celdas a buscar (ID Nota, Materia, Estudiante, Nota) - Columnas 0, 1, 2, 3
                let cellsToSearch = [row.cells[0], row.cells[1], row.cells[2], row.cells[3]];
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
