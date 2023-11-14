#!/usr/bin/node
/* prints the numberof arguments already printed and the new argument value */
let count = 0
exports.logMe = function (item) {
    if (item !== undefined) {
        console.log(`${count}: ${item}`);
    }
    count += 1;
}

module.exports = { logMe };
