#!/usr/bin/node
const url = process.argv[2];
const request = require('request');
request(url, function (err, response, body) {
  if (err) {
    console.error(err);
  }
  let list = [];
  const result = JSON.parse(body).results;
  for (const film of result) {
    list = list.concat(film.characters);
  }
  const uniq = list.filter(x => x === 'https://swapi.co/api/people/18/');
  console.log(uniq.length);
}
);
