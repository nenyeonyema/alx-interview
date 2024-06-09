#!/usr/bin/node
// StarWars API

const request = require('request');

// Get the movie ID from the command line arguments
const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a movie ID.');
  process.exit(1);
}

// URL for the Star Wars API film endpoint with the given movie ID
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Function to fetch character data
const fetchCharacterName = (url) => {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        const characterData = JSON.parse(body);
        resolve(characterData.name);
      }
    });
  });
};

// Fetch the movie details
request(apiUrl, async (error, response, body) => {
  if (error) {
    console.error('Error fetching movie data:', error);
    return;
  }

  if (response.statusCode === 200) {
    const movieData = JSON.parse(body);
    const characterUrls = movieData.characters;

    // Fetch and print each character's name
    for (const url of characterUrls) {
      try {
        const characterName = await fetchCharacterName(url);
        console.log(characterName);
      } catch (error) {
        console.error('Error fetching character data:', error);
      }
    }
  } else {
    console.error(`Error: Received status code ${response.statusCode}`);
  }
});
