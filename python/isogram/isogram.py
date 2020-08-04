def is_isogram(string):
    string = string.replace(' ', '')
    string = string.replace('-', '')
    string = string.lower()
    unique = set(string)
    if len(unique) != len(string):
        return False
    else:
        return True

