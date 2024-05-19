from prefect import flow
from task import get_location,get_single_character, get_characters_info



@flow(name="FlowLocation")
def get_location_info():

    id_location = input('Informe o ID da Localizacao')

    location = get_location(id_location)
    print('------------------- Location --------------------')
    print(location)


@flow(name="FlowSingleCharacter")
def get_single():

    id_character = input('Informe o ID do Personagem')
    repo_json = get_single_character(id_character)
    name      = repo_json['name']
    species   = repo_json['species']
    
    print('------------------- Single Character --------------------')
    print(repo_json)

    return name,species


@flow(name="FlowCharacterFull")
def get_character():
    name,species = get_single()
    character_info = get_characters_info(name,species)

    print('------------------- Character_Info --------------------')
    print(character_info)


if __name__ =="__main__":
    get_character()