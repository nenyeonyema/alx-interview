#!/usr/bin/env python3

import sys
import requests

def get_movie_characters(movie_id):
    base_url = 'https://swapi-api.alx-tools.com/api'
    film_url = f'{base_url}/films/{movie_id}/'
    response = requests.get(film_url)
    
    if response.status_code != 200:
        print(f"Failed to retrieve movie with ID {movie_id}")
        return
    
    film_data = response.json()
    character_urls = film_data.get('characters', [])
    
    for url in character_urls:
        character_response = requests.get(url)
        if character_response.status_code == 200:
            character_data = character_response.json()
            print(character_data['name'])
        else:
            print(f"Failed to retrieve character data from {url}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-starwars_characters.py <Movie ID>")
        sys.exit(1)
    
    movie_id = sys.argv[1]
    get_movie_characters(movie_id)
