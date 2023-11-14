#!/usr/bin/node
/* Prints the first argument passed to it:
If no arguments are passed to the script, print "No argument" */

const args = process.argv.slice(2);
if (args.length === 0) {
  console.log('No argument');
} else {
  console.log(`${args[0]}`);
}
