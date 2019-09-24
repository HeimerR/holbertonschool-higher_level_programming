#!/usr/bin/node
const file = process.argv[2];
const fs = require('fs');
fs.readFile(file, 'utf-8', (err, data) => {
  if (err) {
    console.log('{ Error: ENOENT: no such file or directory, open \'' + file + '\'\n    at Error (native)\n  errno: -2,\n  code: \'ENOENT\',\n  syscall: \'open\',\n  path: \'doesntexist\' }');
  } else {
    process.stdout.write(data);
  }
});
