#!/usr/bin/node
/* This script that prints the addition of 2 integers
The first argument is the first integer
The second argument is the second integer
You have to define a function with this prototype: function add(a, b) */

function add (a, b) {
  const args = process.argv.slice(2);
  a = parseInt(args[0]);
  b = parseInt(args[1]);
  console.log(a + b);
}
add();
