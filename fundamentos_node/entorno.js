#!/usr/bin/env node
/*ATRAPANDO VARIABLES DE ENTORNO EJECUTAR CON ASI:
    NOMBRE=Camilo WEB=bayona.me ./entorno.js o imprimir por defecto*/
let nombre = process.env.NOMBRE || 'No tiene nombre GOT';
let web = process.env.WEB || 'Bayona.me';

console.log('Hola '+ nombre);
console.log('Mi web es ' + web);
console.log('Hola Nodemon');