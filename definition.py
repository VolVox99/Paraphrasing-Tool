from requests import get
from json import loads

def get_definition(word: str) -> str:
    try:
        response = get(f'https://api.dictionaryapi.dev/api/v2/entries/en_US/{word}')
        json_res = loads(response.content)
        #ends with a period so remove last character
        definition = json_res[0]['meanings'][0]['definitions'][0]['definition'][:-1]
        #first letter is capitalized and we dont want that
        return definition[0].lower() + definition[1:]
      
    except:
        return word