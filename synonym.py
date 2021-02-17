from requests import get
from json import loads
from bs4 import BeautifulSoup

def get_synonym(word: str) -> str:
    try:
        html_doc = get(f'https://www.thesaurus.com/browse/{word}')

        soup = BeautifulSoup(html_doc.content.decode(html_doc.encoding), 'lxml')
        script_tags = soup('script')
        synonyms_script_tag = None
        #this is the start of the script tag that contains the synonyms
        syn_list_identifier = 'window.INITIAL_STATE = '
        for tag in script_tags:
            if syn_list_identifier in str(tag):
                synonyms_script_tag = tag
                break

        data = synonyms_script_tag.contents[0].replace(syn_list_identifier, '').replace('undefined', 'null').replace(';', '')
        json_data = loads(data)
        synonyms = json_data['searchData']['tunaApiData']['posTabs'][0]['synonyms']

        return synonyms[0]['term']
    
    except:
        return word