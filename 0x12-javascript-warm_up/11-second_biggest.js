#!/usr/bin/node
if (process.argv[2] === undefined || (process.argv[3] === undefined)) {
  console.log('0');
} else {
  process.argv.shift();
  process.argv.shift();
  const array = [...new Set(process.argv.sort().reverse())];
  if (array.length === 1) {
    console.log('0');
  } else {
    console.log(array[1]);
  }
}
