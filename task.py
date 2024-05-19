from prefect import task
from util.http import http
from requests.exceptions import Timeout
import time

@task
def get_location(id_location: int):     
        urlApiInfo = "https://rickandmortyapi.com/api/location"
        response = http.get(f'{urlApiInfo}/{id_location}')
        
        if response.status_code == 200: 
            repo = response.json()
            return repo

 

@task
def get_single_character(id_character: int):
    urlApSingleCharacter = f"https://rickandmortyapi.com/api/character"
    response = http.get(f'{urlApSingleCharacter}/{id_character}')
    
    if response.status_code == 200:
        repo = response.json()
        return repo

@task 
def get_characters_info(name_character: str, species_character: str):

    urlApiCharacterInfo = f'https://rickandmortyapi.com/api/character/?name={name_character}&species={species_character}'
    response = http.get(urlApiCharacterInfo)
    if response.status_code == 200:
        repo = response.json()
        return repo
