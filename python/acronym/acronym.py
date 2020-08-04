from re import sub


def abbreviate(words):
    words = sub("[^a-zA-Z0\- ]", "", words)
    words = sub("-", " ", words)
    words = words.split()
    acronym = str()
    for word in words:
        acronym += word[0].upper()
    return acronym
