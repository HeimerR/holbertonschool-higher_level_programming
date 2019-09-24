#!/usr/bin/node
const url = process.argv[2];
const file = process.argv[3];
const request = require('request');
const fs = require('fs');
request(url, function (err, response, body) {
  if (err) {
    throw err;
  } else {
    fs.appendFile(file, body, 'utf-8', function (err, data) {
      if (err) {
        throw err;
      }
    });
  }
}
);
