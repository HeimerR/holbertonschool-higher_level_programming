#!/usr/bin/node
const url = process.argv[2];
const request = require('request');
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    let list = [];
    for (const film of JSON.parse(body).results) {
      list = list.concat(film.characters);
    }
    // console.log(list);
    const uniq = list.filter(x => x === 'https://swapi.co/api/people/18/');
    console.log(uniq.length);
  }
}
);
