def is_pangram(sentence):
    alphas = set()
    for char in sentence:
        if char.isalpha():
            alphas.add(char.lower())
    print(alphas)
    return True if len(alphas) == 26 else False

