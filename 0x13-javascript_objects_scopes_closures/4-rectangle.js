#!/usr/bin/node
/* This defines an empty class Rectangle */
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const row = 'X'.repeat(this.width);
    for (let y = 0; y < this.height; y++) {
      console.log(`${row}`);
    }
  }

  rotate () {
    const aux = this.width;
    this.width = this.height;
    this.height = aux;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

module.exports = Rectangle;
