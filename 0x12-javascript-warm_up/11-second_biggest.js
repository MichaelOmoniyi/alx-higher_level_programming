#!/usr/bin/node
/* This script that searches the second biggest integer in the list of arguments.
You can assume all arguments can be converted to integer
If no argument passed, print 0
If the number of arguments is 1, print 0 */

const args = process.argv.slice(2);

if (args.length === 0) {
  console.log(0);
} else {
  const integers = args.map(Number);
  const sortedIntegers = integers.sort((a, b) => b - a);
  const uniqueSortedIntegers = [...new Set(sortedIntegers)];

  if (uniqueSortedIntegers.length === 1) {
    console.log(0);
  } else {
    console.log(uniqueSortedIntegers[1]);
  }
}
