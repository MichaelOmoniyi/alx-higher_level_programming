#!/usr/bin/node
/* Imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence. */

const data = require('./101-data');
const dict = data.dict;
const occurrences = {};

Object.keys(dict).forEach(key => {
    const occurrenceCount = dict[key];
    if (!occurrences[occurrenceCount]) {
        occurrences[occurrenceCount] = [key];
    } else {
        occurrences[occurrenceCount].push(key);
    }
});

console.log(occurrences);
