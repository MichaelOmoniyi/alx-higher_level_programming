#!/usr/bin/node
/* Prints the first argument passed to it:
If no arguments are passed to the script, print "No argument" */

const args = process.argv.slice(2);
console.log(`${args[0]}`);
