#!/usr/bin/node
/* Imports an array and computes a new array */
const list = require('./100-data.js').list;
const newArr = list.map((value, index) => value * index);
console.log(list);
console.log(newArr);
