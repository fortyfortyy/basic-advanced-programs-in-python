def pairs_sum_to_target(list1, list2, target):
    """
    Function that accepts two lists of integers and a target integer named target and returns all pairs of indices
    in the form [x, y] where list1[x] + list2[y] == target. In other words, return the pairs of indices where the sum
    of their values equals target.
    """
    pairs = []

    for index_one, first_number in enumerate(list1):
        for index_two, second_number in enumerate(list2):
            if first_number + second_number == target:
                pairs.append([index_one, index_two])

    return pairs


list1 = [1, -2, 4, 5, 9]
list2 = [4, 2, -4, -4, 0]
target = 5
e = pairs_sum_to_target(list1, list2, target)
print(e)
