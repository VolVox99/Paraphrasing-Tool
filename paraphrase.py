from synonym import get_synonym
from definition import get_definition
from ignore import should_ignore


def methodical_compute_word(idx, word):
    #dont want anything different for first word
    if not idx or should_ignore(word): return word

    if not idx % 3:
        return get_synonym(word)
    
    elif not idx % 7:
        return get_definition(word)

    return word

def paraphrase(text: str):
    output = []
    for idx, word in enumerate(text.split(' ')):
        if not word: continue

        output.append(methodical_compute_word(idx, word))
        
       
    return ' '.join(output)
        

def main():
   with open('input.txt') as in_file:
       with open('output.txt', 'w') as out_file:
           out_file.write(paraphrase(in_file.read()))


if __name__ == '__main__':
    main()