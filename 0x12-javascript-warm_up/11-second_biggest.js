#!/usr/bin/node
if (process.argv[2] === undefined || (process.argv[3] === undefined)) {
  console.log('0');
} else {
  process.argv.shift();
  process.argv.shift();
  console.log(process.argv);
  const array = process.argv.map(Number).sort((a, b) => a - b).reverse();
  console.log(array[1]);
}
