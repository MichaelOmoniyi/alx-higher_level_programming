#!/usr/bin/node
/* Prints the first argument passed to it:
If no arguments are passed to the script, print "No argument" */

const args = process.argv.slice(2);
if (args[0]) {
  console.log(`${args[0]}`);
} else {
  console.log('No argument');
}
