#!/usr/bin/node
const url = process.argv[2];
const request = require('request');
request(url, function (err, response, body) {
  if (err) {
    throw err;
  } else {
    const dict = {};
    for (const obj of JSON.parse(body)) {
      if (obj.completed) {
        if (dict[obj.userId]) {
          dict[obj.userId]++;
        } else {
          dict[obj.userId] = 1;
        }
      }
    }
    console.log(dict);
  }
});
