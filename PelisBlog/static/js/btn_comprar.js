// Obtén una referencia al botón "Comprar" por su id
var btnComprar = document.getElementById("btn-comprar");

// Agrega un evento click al botón
btnComprar.addEventListener("click", function () {
    var id = document.querySelector(".id-peli").textContent;
    // Obtén la fecha actual
    var fecha = new Date().toLocaleDateString();

    // Obtén el nombre de la película del elemento con la clase "nombre-peli"
    var nombrePelicula = document.querySelector(".nombre-peli").textContent;

    // Obtén el precio de la película del elemento con la clase "precio"
    var precioPelicula = document.querySelector(".precio").textContent;

    // Crea un objeto que contenga los datos
    var datosCompra = {
        id: id,
        fecha: fecha,
        nombre: nombrePelicula,
        precio: precioPelicula
    };

    // Convierte el objeto a formato JSON
    var datosCompraJSON = JSON.stringify(datosCompra);

    // Almacena los datos en el almacenamiento local del navegador
    localStorage.setItem("datosCompra", datosCompraJSON);

    // Ejemplo: muestra una alerta con los datos almacenados
    //alert("Datos de compra almacenados:\nFecha: " + fecha + "\nNombre: " + nombrePelicula + "\nPrecio: " + precioPelicula);
});
