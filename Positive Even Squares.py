def positive_even_squares(*args):
    """
    Function that accepts any number of positional arguments, all of which may assue will be lists of integers. Function
    filter all of these lists such taht they only contain even positive integers and combine all the list into one
    list of integers and squares all the elements and return that list.
    :param args:
    :return: list of squared numbers
    """

    positive_even_nums = []

    for lst in args:
        filter_list = list(filter(lambda number: number > 0 and number % 2 == 0, lst))
        positive_even_nums.extend(filter_list)

    return list(map(lambda num: num ** 2, positive_even_nums))


args = [[-5, 2, 3, 4, 5], [1, 3, 5, 6, 7], [-9, -8, 10]]
a = positive_even_squares(*args)
print(a)
