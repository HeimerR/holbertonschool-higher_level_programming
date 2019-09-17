#!/usr/bin/node
let n = Number(process.argv[2]);
if (Number.isNaN(n)) {
  console.log('Missing size');
} else if (n > 0) {
  let str = '#'.repeat(n);
  for (let i = 0; i < n; i++) {
    console.log(str);
  }
}
