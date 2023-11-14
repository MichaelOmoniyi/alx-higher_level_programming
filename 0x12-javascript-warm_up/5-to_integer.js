#!/usr/bin/node
/* Prints My number: <first argument converted in integer> if the first argument can be converted to an integer:
If the argument can’t be converted to an integer, print "Not a number" */

const args = process.argv.slice(2);

const firstArgument = args[0];
const intArgs = parseInt(firstArgument);

if (!isNaN(intArgs)) {
  console.log(`My number: ${intArgs}`);
} else {
  console.log('Not a number');
}
