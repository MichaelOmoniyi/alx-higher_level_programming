#!/usr/bin/node
const Rectangle = require('./4-rectangle');

/* This defines an empty class Square */
class Square extends Rectangle {
    constructor(size) {
        super(size, size);
    }
    charPrint(c) {
        if (c === undefined) {
            c = 'X';
        }

        for(let y = 0; y < this.height; y++) {
            let row = '';
            for(let x = 0; x < this.width; x++) {
                row += c;
            }
            console.log(row);
        }
    }
}

module.exports = Square;
