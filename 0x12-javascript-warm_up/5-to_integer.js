#!/usr/bin/node
let n = Number(process.argv[2]);
if (Number.isNaN(n)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + n);
}
