# Consider using strip on the phrase as the first thing you do in the hey function. Then is_empty becomes trivial.
# Consider using isupper for is_yelling
# Consider using endswith for is_question

def hey(phrase):
    """
        Have Bob respond based on the phrase.
    """
    if is_empty(phrase):
        return "Fine. Be that way!"
    asking_question = is_question(phrase)
    yelling = is_yelling(phrase)
    if asking_question and yelling:
        return "Calm down, I know what I'm doing!"
    elif asking_question:
        return "Sure."
    elif yelling:
        return "Whoa, chill out!"
    return "Whatever."

def is_empty(phrase):
    """
        Evaluate for non-responses. Non-responses are empty strings or strings consisting only of spaces, tabs, and newline characters.
    """
    empty_chars = " \n\t\r"
    for char in phrase:
        if char not in empty_chars:
            return False
    return True

def is_yelling(phrase):
    """
        Check if the speaker is yelling. Yelling means uppercase letters are present and lowercase letters are not present.
    """
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    has_uppercase_letters = False
    has_no_lowercase_letters = True
    for char in phrase:
        if char in uppercase:
            has_uppercase_letters = True
        elif char in lowercase:
            has_no_lowercase_letters = False
    if has_uppercase_letters and has_no_lowercase_letters:
        return True
    return False

def is_question(phrase):
    """
        Check if the last character is a question mark. Trailing whitespace does not count.
    """
    last_char = phrase.rstrip()[-1]
    if last_char == "?":
        return True
    return False