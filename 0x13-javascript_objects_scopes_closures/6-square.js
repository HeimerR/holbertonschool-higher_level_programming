#!/usr/bin/node
const SquareBase = require('./5-square');
class Square extends SquareBase {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let s = '';
    for (let i = 0; i < this.width; i++) {
      for (let j = 0; j < this.width; j++) {
        s += c;
      }
      s += '\n';
    }
    console.log(s.slice(0, -1));
  }
}
module.exports = Square;
