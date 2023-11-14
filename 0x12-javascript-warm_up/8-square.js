#!/usr/bin/node
/* The script that prints a square
The first argument is the size of the square
If the first argument can’t be converted to an integer, print “Missing size”
You must use the character X to print the square */

const args = process.argv.slice(2);
const firstArg = args[0];
const size = parseInt(firstArg);

if (isNaN(size)) {
  console.log('Missing size');
} else {
  const row = 'X'.repeat(size);
  for (let i = 0; i < size; i++) {
    console.log(row);
  }
}
