#!/usr/bin/node
const episode = process.argv[2];
const url = 'http://swapi.co/api/films/' + episode;
const request = require('request');
request(url, function (err, response, body) {
  if (err) {
    throw err;
  } else {
    console.log(JSON.parse(body).title);
  }
}
);
