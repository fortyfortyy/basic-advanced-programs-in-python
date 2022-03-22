def create_strings_from_characters(frequencies, string1, string2):
    """
    Function that accepts a dictionary called frequencies and two strings. The frequencies' dictionary contains
    character keys and integer values, the value associated with each character represents its frequency. Function
    returns 0, 1, 2 according to the frequencies of characters in the dictionary is sufficient or not to create string1
    and (or) string2 without reusing any characters.
    """

    can_create_string1 = can_create_string_from_frequencies(
        frequencies, string1)
    can_create_string2 = can_create_string_from_frequencies(
        frequencies, string2)

    if (not can_create_string1) or (not can_create_string2):
        if can_create_string1 or can_create_string2:
            return 1

        return 0

    for character in string1 + string2:
        if character not in frequencies or frequencies[character] == 0:
            return 1

        frequencies[character] -= 1

    return 2


def can_create_string_from_frequencies(frequencies, string):
    for character in set(string):
        if string.count(character) > frequencies.get(character, 0):
            return False

    return True


frequencies = {"h": 2, "e": 1, "l": 1, "r": 4, "a": 3, "o": 2, "d": 1, "w": 1}
string1 = "hello"
string2 = "world"
e = create_strings_from_characters(frequencies, string1, string2)
print(e)
