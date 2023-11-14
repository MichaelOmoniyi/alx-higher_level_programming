#!/usr/bin/node
/* This function that increments and calls a function.
The function must be visible from outside */

function addMeMaybe(number, theFunction) {
    number += 1;
    theFunction(number);
}
module.exports = { addMeMaybe }
