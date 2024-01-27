
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


var contadorCamposA = 0;

function agregarElemento(tipo) {
    var selectElement;
    var container;

    if (tipo === 'actividad') {
        selectElement = document.getElementById('actividades');
        container = document.getElementById('actividadesContainer');

        // Obtener el elemento seleccionado
        var elementoSeleccionado = selectElement.options[selectElement.selectedIndex].text;
        var elementoSeleccionadoId = selectElement.options[selectElement.selectedIndex].value;

        // Verificar si el elemento ya está en el contenedor
        if (!contieneElemento(container, elementoSeleccionado)) {
            // Crear un contenedor para el elemento con un botón de eliminación
            var elementoContainer = document.createElement('div');
            elementoContainer.className = 'col-lg-12 d-flex flex-column mb-2';
            elementoContainer.innerHTML = `
                  <div class="col-lg-12 d-flex justify-content-between align-items-start mb-2">
                    <div>
                      <span>${contadorCamposA}.&nbsp;</span>
                      ${elementoSeleccionado}
                      <input type="hidden" name = "actividad${contadorCamposA}" value="${elementoSeleccionadoId}" readonly style="border:0; background-color: white; cursor: default; pointer-events: none;" id="id_actividad${contadorCamposA}">
                    </div>
                    <button type="button" class="col-lg-2 btn-close " aria-label="Close" onclick="eliminarElemento(this)"></button>
                  </div>`;
            container.appendChild(elementoContainer);

        }
    }
}

function contieneElemento(container, elemento) {
    var elementos = container.getElementsByTagName('div');

    for (var i = 0; i < elementos.length; i++) {
        if (elementos[i].textContent.includes(elemento)) {
            // El elemento ya está en el contenedor
            return true;
        }
    }
    // El elemento no está en el contenedor
    // Incrementar el contador de campos después de agregar
    contadorCamposA++;
    return false;
}

function eliminarElemento(btn) {
    var container = btn.parentNode.parentNode; // Obtener el contenedor padre del botón

    // Eliminar el contenedor del elemento
    container.removeChild(btn.parentNode);

}
