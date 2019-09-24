#!/usr/bin/node
const file = process.argv[2];
const fs = require('fs');
fs.readFile(file, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    process.stdout.write(data);
  }
});
