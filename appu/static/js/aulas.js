document.addEventListener('DOMContentLoaded', function() {
    console.log('Script de aulas cargado correctamente');

    
    // 1. Manejo de la modal de eliminación
    const confirmDeleteAulaModal = document.getElementById('confirmDeleteAulaModal');
    if (confirmDeleteAulaModal) {
        const confirmDeleteAulaButton = document.getElementById('confirmDeleteAulaButton');
        confirmDeleteAulaModal.addEventListener('show.bs.modal', function(event) {
            // Botón que disparó el modal (el botón de eliminar en la fila de la tabla)
            const button = event.relatedTarget;
            // Obtener el ID del aula del atributo data-aula-id
            const aulaId = button.getAttribute('data-aula-id');

            if (confirmDeleteAulaButton && aulaId) {
                confirmDeleteAulaButton.href = `/deleteaula/${aulaId}`; // Ajusta esta URL si tu patrón es diferente
            }
        });
    }

    // 2. Funcionalidad de búsqueda en la tabla de aulas
    const searchInput = document.getElementById('searchInputAulas');
    const aulasTable = document.getElementById('aulasTable');

    if (searchInput && aulasTable) {
        searchInput.addEventListener('keyup', function() {
            const searchText = this.value.toLowerCase();
            const rows = aulasTable.getElementsByTagName('tbody')[0].getElementsByTagName('tr');

            for (let i = 0; i < rows.length; i++) {
                let row = rows[i];
                let cells = row.getElementsByTagName('td');
                let found = false;

                const cellsToSearch = [0, 1, 2, 3, 4, 5]; // IDs, Capacidad, Aire, Videobeam, Pizarra, Ubicación

                for (let j = 0; j < cellsToSearch.length; j++) {
                    const cellIndex = cellsToSearch[j];
                    if (cells[cellIndex]) { // Asegúrate de que la celda exista
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
