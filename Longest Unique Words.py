def get_n_longest_unique_words(words, n):
    """
    Function that accepts a list of strings that represent words and a positive integer n, representing the number of
    unique words to return. Function returns a new list containing the n longest unique words from the input list.
    """

    unique_list = []
    for word in words:
        if words.count(word) == 1:
            unique_list.append(word)

    sorted_words = sorted(unique_list, key=len, reverse=True)
    return sorted_words[:n]


words = ["Longer", "Whatever", "Longer",
         "Ball", "Rock", "Rocky", "Rocky"]
n = 1
e = get_n_longest_unique_words(words, n)
print(e)
