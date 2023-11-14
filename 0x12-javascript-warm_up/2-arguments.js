#!/usr/bin/node
// prints a message depending of the number of arguments passed
const args = process.argv.slice(2);
const argsLen = args.length;

if (argsLen === 0) {
  console.log('No argument');
} else if (argsLen === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
