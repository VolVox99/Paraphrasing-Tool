
def should_ignore(word: str) -> bool:
    with open('ignorelist.txt') as file:
        words_to_ignore = file.readlines()


    conditions = [
        #if all chars are not letters from alphabet
        not word.isalpha(),
        word.lower() in words_to_ignore,
        word.isnumeric(),
        #if first letter is capital = proper noun
        word[0].isupper()
    ]


    return any(conditions)