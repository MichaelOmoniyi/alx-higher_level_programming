#!/usr/bin/node
const SquareEx = require('./5-square.js');

/* This defines an empty class Square */
class Square extends SquareEx {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }

    for (let y = 0; y < this.height; y++) {
      let row = '';
      for (let x = 0; x < this.width; x++) {
        row += c;
      }
      console.log(row);
    }
  }
}

module.exports = Square;
