#!/usr/bin/node
const url = process.argv[2];
const id = 18;
const request = require('request');
request(url, function (err, response, body) {
  if (err) {
    throw err;
  } else {
    let counter = 0;
    for (const film of JSON.parse(body).results) {
      if (film.characters.includes('https://swapi.co/api/people/' + id + '/')) {
        counter++;
      }
    }
    console.log(counter);
  }
}
);
