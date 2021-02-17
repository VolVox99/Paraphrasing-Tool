def should_ignore(word: str) -> bool:
    with open('ignorelist.txt') as file:
        words = file.readlines()
    
    return word.lower() in words
    