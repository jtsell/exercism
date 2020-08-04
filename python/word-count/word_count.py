from re import sub


def word_count(phrase: str) -> dict:
    count = dict()
    phrase = phrase.casefold()
    phrase = sub("[^a-z0-9_,\s']", "", phrase)
    phrase = sub("[\t\n_,]", " ", phrase)
    phrase = sub("( ')|(' )|('$)|(^')", " ", phrase)
    words = phrase.split()
    for word in words:
        count[word] = words.count(word)
    return count
