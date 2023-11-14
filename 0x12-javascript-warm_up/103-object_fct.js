#!/usr/bin/node
/* This script by adding a new function incr that increments the integer value. */
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
function incr() {
  myObject.value += 1;
}
myObject.incr = incr;
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
