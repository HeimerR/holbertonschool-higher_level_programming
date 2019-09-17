#!/usr/bin/node
let n = parseInt(process.argv[2]);
if (isNaN(n) === true) {
  console.log('Not a number');
} else {
  console.log('My number: ' + n);
}
