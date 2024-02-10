
var contadorCampos = 1;
var limiteCampos = 11;

function agregarCampos() {
    var camposContainer = document.getElementById('camposContainer');

    if (contadorCampos < limiteCampos) {
        // Crear un nuevo div con los campos
        var nuevoDiv = document.createElement('div');
        nuevoDiv.className = 'border border-4 rounded p-3 mb-3';

        // Campos
        nuevoDiv.innerHTML = `
      <div class="col-lg-12 mb-3" for="Otrosicontador ${contadorCampos}">Otrosis número ${contadorCampos}:</div>

      <label for="adiccion${contadorCampos}">Adicción:</label>
      <input type="text" class="form-control mb-2" id="adiccion${contadorCampos}">

      <label for="prorroga${contadorCampos}">Prórroga:</label>
      <input type="text" class="form-control mb-2" id="prorroga${contadorCampos}">

      <label for="OtrosiActividad${contadorCampos}">Actividad:</label>
      <input type="text" class="form-control mb-2" id="OtrosiActividad${contadorCampos}">

      <label for="fechaTerminacion${contadorCampos}">Fecha de Terminación:</label>
      <input type="date" class="form-control mb-2" id="fechaTerminacion${contadorCampos}">
    `;

        // Incrementar el contador de campos
        contadorCampos++;

        // Agregar el nuevo div al contenedor
        camposContainer.appendChild(nuevoDiv);
    } else {
        alert('Se ha alcanzado el límite de 10 campos de otrosis.');
    }
}

function eliminarCampo() {
    var camposContainer = document.getElementById('camposContainer');
    if (contadorCampos > 1) {
        // Decrementar el contador de campos
        contadorCampos--;

        // Obtener el último div y eliminarlo
        var ultimoDiv = camposContainer.lastChild;
        camposContainer.removeChild(ultimoDiv);
    }
}



// <!-- Script para agregar actividades-->


let contadorCamposA = 0;

// function agregarElemento(tipo) {
//     var selectElement;
//     var container;

//     if (tipo === 'actividad') {
//         selectElement = document.getElementById('actividades');
//         container = document.getElementById('actividadesContainer');

//         // Crear un contenedor para el elemento con un botón de eliminación
//         var elementoContainer = document.createElement('div');
//         elementoContainer.className = 'col-lg-12 d-flex mb-2';
//         elementoContainer.innerHTML = `
//                   <div class="col-lg-12 justify-content-between align-items-start mb-2">
//                     <div class="col-lg-10">
//                         <textarea name = "actividad${contadorCamposA}" required class="form-control col-lg-10" style="max-width:100%" id="id_actividad${contadorCamposA++}" rows="4"> </textarea>
//                         <button type="button" class=" btn-close col-lg-2 " aria-label="Close" onclick="eliminarElemento(this)"></button>
//                     </div>
//                   </div>`;
//         container.appendChild(elementoContainer);
//     }
// }
function agregarElemento(tipo) {
    var selectElement;
    var container;

    if (tipo === 'actividad') {
        selectElement = document.getElementById('actividades');
        container = document.getElementById('actividadesContainer');

        // Crear un contenedor para el elemento con un botón de eliminación
        var elementoContainer = document.createElement('div');
        elementoContainer.className = 'col-lg-12 col-md-12 col-sm-12 d-flex mb-2';
        elementoContainer.innerHTML = `
            <div class="col-lg-12 col-md-12 col-sm-12 justify-content-between align-items-start mb-2">
                <div class="col-lg-12 col-md-12 col-sm-12">
                    <div class="input-group">
                        <textarea name="actividad${contadorCamposA}" required class="form-control" id="id_actividad${contadorCamposA}" rows="4"></textarea>
                        <button type="button" class="btn-close" aria-label="Close" onclick="eliminarElemento(this)"></button>
                    </div>
                </div>
            </div>`;
        container.appendChild(elementoContainer);
    }
    contadorCamposA++
}

function eliminarElemento(elemento) {
    // Eliminar el contenedor del elemento padre
    var container = elemento.closest('.col-lg-12');
    container.parentNode.removeChild(container);
}



function eliminarElemento(btn) {
    var container = btn.parentNode.parentNode; // Obtener el contenedor padre del botón

    // Eliminar el contenedor del elemento
    container.removeChild(btn.parentNode);

}
function abrir_modal_edicion(url) {
    $('#miModal').load(url, function () {
        $('#miModal').modal('show');
    });
}
// Cuando se hace clic en el botón de cerrar, ocultar el modal
$("#cerrarModal").click(function () {
    $("#miModal").hide();
});

