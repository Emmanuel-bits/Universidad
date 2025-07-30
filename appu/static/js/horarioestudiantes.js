document.addEventListener('DOMContentLoaded', function() {
    console.log('Script de horarios de estudiantes cargado correctamente');


    // 1. Manejo de la modal de eliminación para Horario de Estudiantes
    const confirmDeleteHorarioEstudianteModal = document.getElementById('confirmDeleteHorarioEstudianteModal');
    if (confirmDeleteHorarioEstudianteModal) {
        const confirmDeleteHorarioEstudianteButton = document.getElementById('confirmDeleteHorarioEstudianteButton');
        confirmDeleteHorarioEstudianteModal.addEventListener('show.bs.modal', function(event) {
            const button = event.relatedTarget; // Botón que activó el modal
            const horarioEstudianteId = button.getAttribute('data-horarioestudiante-id'); // Obtener el ID del horario
            if (confirmDeleteHorarioEstudianteButton && horarioEstudianteId) {
                // Actualizar el href del botón de eliminación en el modal
                confirmDeleteHorarioEstudianteButton.href = `/deletehorarioestudiante/${horarioEstudianteId}`;
            }
        });
    }

    // 2. Funcionalidad de búsqueda en la tabla de Horarios de Estudiantes
    const searchInputHorarioEstudiantes = document.getElementById('searchInputHorarioEstudiantes');
    const horarioEstudiantesTable = document.getElementById('horarioEstudiantesTable');

    if (searchInputHorarioEstudiantes && horarioEstudiantesTable) {
        searchInputHorarioEstudiantes.addEventListener('keyup', function() {
            const searchText = this.value.toLowerCase();
            const rows = horarioEstudiantesTable.getElementsByTagName('tbody')[0].getElementsByTagName('tr');

            for (let i = 0; i < rows.length; i++) {
                let row = rows[i];
                let cells = row.getElementsByTagName('td');
                let found = false;

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
