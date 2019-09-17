#!/usr/bin/node
function add (a, b) {
  return (a + b);
}
let a = Number(process.argv[2]);
let b = Number(process.argv[3]);
console.log(add(a, b));
