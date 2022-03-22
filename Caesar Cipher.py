def caesar_cipher(string, offset):
    """
    Function that accepts a string and returns the caesar cipher encoding of that string according to a secondary input
    parameter named offset.
    """

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    encoded_string = ''

    for character in string:
        position = alphabet.index(character)
        encoded_string += alphabet[position - offset]

    return encoded_string


string = 'hello'
offset = 3
caesar_cipher(string, offset)

string = 'ab'
offset = 2
caesar_cipher(string, offset)
