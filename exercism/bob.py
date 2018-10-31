def hey(phrase):
    """
        Have Bob respond based on the phrase.
    """
    stripped_phrase = phrase.strip()
    asking_question = stripped_phrase.endswith("?")
    yelling = stripped_phrase.isupper()
    if stripped_phrase == "":
        return "Fine. Be that way!"
    elif asking_question and yelling:
        return "Calm down, I know what I'm doing!"
    elif asking_question:
        return "Sure."
    elif yelling:
        return "Whoa, chill out!"
    return "Whatever."