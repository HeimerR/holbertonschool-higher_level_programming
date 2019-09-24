#!/usr/bin/node
const file = process.argv[2];
const fs = require('fs');
fs.readFile(file, 'utf-8', (err, data) => {
  if (err) {
    console.log('{ Error: ENOENT: no such file or directory, open \'' + file + '\'\n\t\tat Error (native)\n\terrno: -2,\n\tcode: \'ENOENT\',\n\tsyscall: \'open\',\n\tpath: \'doesntexist\' }');
  } else {
    process.stdout.write(data);
  }
});
