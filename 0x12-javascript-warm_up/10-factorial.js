#!/usr/bin/node
/* This script that computes and prints a factorial
The first argument is integer (argument can be cast as integer) used for computing the factorial
Factorial of NaN is 1
You must do it recursively
You must use a function */

const args = process.argv.slice(2);
const num = parseInt(args[0]);
function factorial (num) {
  if (num < 0 || isNaN(num)) {
    return 1;
  } else if (num === 0) {
    return 1;
  } else {
    return ((num * factorial(num - 1)));
  }
}
const result = factorial(num);
console.log(result);
