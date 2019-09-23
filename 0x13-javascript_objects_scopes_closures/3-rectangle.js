#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let s = '';
    for (let i = 0; i < this.height; i++) {
      for (let i = 0; i < this.width; i++) {
        s += 'X';
      }
      s += '\n';
    }
    console.log(s.slice(0, -1));
  }
}
module.exports = Rectangle;
