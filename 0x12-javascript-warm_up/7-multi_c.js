#!/usr/bin/node
/* This script that prints x times “C is fun”
Where x is the first argument of the script
If the first argument can’t be converted to an integer, print "Missing number of occurrences" */

const args = process.argv.slice(2);
const firstArg = args[0];
const firstArgInt = parseInt(firstArg);

if (isNaN(firstArgInt)) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < firstArgInt; i++) {
    console.log('C is fun');
  }
}
