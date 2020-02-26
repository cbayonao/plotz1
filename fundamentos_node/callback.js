#!/usr/bin/env node
function hola(nombre, miCallback) {
    setTimeout(function() {
        console.log('Hola, ' + nombre);
        miCallback(nombre);
    }, 2000);
}

function adios(nombre, otroCallback) {
    setTimeout(function() {
        console.log('Adios', nombre);
        otroCallback();
    }, 1000);
}
/*
Dos funciones asincronas podemos decidir el orden de ejcucion
Una dentro del callback de la otra para que se ejecuten una despues de la otra.
*/
console.log('Iniciando proceso..... ');
hola('Camilo', function (nombre){
    adios(nombre, function () {
        console.log('Terminando proceso.....');
    });
});
/*
Problema de sincronia
*/
// hola('Camilo', function() {});
// adios('Camilo', function() {});