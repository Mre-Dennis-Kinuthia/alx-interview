#!/usr/bin/node

/*
* Prints all characters of a Star Wars movie
* The first positional argument passed is the Movie ID - example: 3 = “Return of the Jedi”
* Displays one character name per line in the same order as the “characters” list in the /films/ endpoint
*/

const request = require('request');

const arg = Number(process.argv[2]);
const url = 'https://swapi-api.alx-tools.com/api/films/' + arg;

if (arg === undefined || isNaN(arg)) {
  console.log('Usage: ./0-starwars_characters NUM');
  process.exit(1);
}

request(url, async (error, response, body) => {
  if (error) {
    console.error('Error: ', error);
    return;
  }

  const parsedBody = JSON.parse(body);
  const characters = parsedBody.characters;

  for (let i = 0; i < characters.length; i++) {
    await new Promise((resolve, reject) => {
      request(characters[i], (error, response, body) => {
        if (error) {
          console.error('Error: ', error);
          return;
        }

        const parsedCharacter = JSON.parse(body);
        console.log(parsedCharacter.name);
        resolve();
      });
    });
  }
});
