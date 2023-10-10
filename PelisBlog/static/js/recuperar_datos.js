// Recuperar datos del localStorage
var datosCompraJSON = localStorage.getItem("datosCompra");
if (datosCompraJSON) {
    var datosCompra = JSON.parse(datosCompraJSON);
    // Acceder a los datos y mostrarlos en la página
    document.getElementById("fecha").textContent = datosCompra.fecha;
    document.getElementById("nombre").textContent = datosCompra.nombre;
    document.getElementById("precio").textContent = datosCompra.precio;
} else {
    // Si no hay datos, crea una lista vacía
    var miLista = [];
}

// Paso 3: Agrega un nuevo elemento a la lista
var nuevoElemento = 'Nuevo elemento';
miLista.push(nuevoElemento);

localStorage.setItem('miLista', JSON.stringify(miLista));
