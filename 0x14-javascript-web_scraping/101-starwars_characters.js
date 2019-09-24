#!/usr/bin/node
const id = process.argv[2];
const url = 'http://swapi.co/api/films/' + id;
const request = require('request');
request(url, function getList(err, response, body) {
  if (err) {
    throw err;
  } else {
    list = [];
    JSON.parse(body).characters.forEach( async function (urlChar) {
      let res = await request(urlChar, function getChar(err2, response2, body2) {
        if (err2) {
          throw err2;
        } else {
          list.push(JSON.parse(body2).name);
        }
      });
    });
    console.log(list);
  }
});
