def is_pangram(sentence):
    character_hash = {}
    for char in sentence:
        if char in "abcdefghhijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            character_hash[lowercase_char] = True
    for letter in "abcdefghijklmnopqrstuvwxyz":
        letter_present = character_hash.get(letter, False)
        if letter_present == False:
            return False
    return True
