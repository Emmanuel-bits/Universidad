document.addEventListener('DOMContentLoaded', function() {
    console.log('Script de materias cargado correctamente');

    // 1. Manejo de la modal de eliminación
    const confirmDeleteMateriaModal = document.getElementById('confirmDeleteMateriaModal');
    if (confirmDeleteMateriaModal) {
        const confirmDeleteMateriaButton = document.getElementById('confirmDeleteMateriaButton');
        confirmDeleteMateriaModal.addEventListener('show.bs.modal', function(event) {
            // Button that triggered the modal
            const button = event.relatedTarget; 
            // Extract info from data-bs-* attributes
            const materiaId = button.getAttribute('data-materia-id');
            
            if (confirmDeleteMateriaButton && materiaId) {
                // Update the modal's delete button href
                confirmDeleteMateriaButton.href = `/deletemateria/${materiaId}`; // Asegúrate de que esta URL coincida con tu urls.py
            }
        });
    }

    // 2. Funcionalidad de búsqueda en la tabla de materias
    const searchInput = document.getElementById('searchInputMaterias');
    const materiasTable = document.getElementById('materiasTable');

    if (searchInput && materiasTable) {
        searchInput.addEventListener('keyup', function() {
            const searchText = this.value.toLowerCase();
            const rows = materiasTable.getElementsByTagName('tbody')[0].getElementsByTagName('tr');

            for (let i = 0; i < rows.length; i++) {
                let row = rows[i];
                let cells = row.getElementsByTagName('td');
                let found = false;

                // Itera sobre las celdas de la fila para buscar el texto (excluye la última celda de 'Acciones')
                // Ajusta el rango 'j < cells.length - X' según el número de columnas que deseas buscar.
                // Por ejemplo, si tienes 5 columnas de datos + 1 de acciones, sería 'j < 5'.
                // En Materia: ID, Nombre, Unidades Créditos, Modalidad, Carrera -> 5 columnas.
                for (let j = 0; j < cells.length - 1; j++) { 
                    let cellText = cells[j].textContent.toLowerCase();
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
