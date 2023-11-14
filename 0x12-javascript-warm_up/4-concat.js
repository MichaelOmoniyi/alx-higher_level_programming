#!/usr/bin/node
/* Prints two arguments passed to it, in the following format: “ is ”
You must use console.log(...) to print all output */

const args = process.argv.slice(2);
console.log(`${args[0]} is ${args[1]}`);
