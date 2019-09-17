#!/usr/bin/node
if (process.argv[2] === undefined || (process.argv[3] === undefined)) {
  console.log('0');
} else {
  process.argv.shift();
  process.argv.shift();
  process.argv.sort().reverse();
  console.log(process.argv[1]);
}
