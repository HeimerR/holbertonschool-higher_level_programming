#!/usr/bin/node
if (isNaN(parseInt(process.argv[2]))) {
  console.log('Missing size');
} else if (parseInt(process.argv[2]) > 0) {
  let str = '#'.repeat(parseInt(process.argv[2]));
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    console.log(str);
  }
}
