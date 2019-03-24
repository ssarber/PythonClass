"""
Write a function that determines whether an array contain a pair
of numbers that sum up to a certain integer and returns that pair
I.e. 10, [3, 4, 1, 2, 8] -> (2, 9)
"""


def contains_sum_of(number, array):
    """Algo: for every number, we know what the number is that need to be added
    to get a sum. Iretate over the array, add every number in the array to a dictionary,
    and see if the summing number is in the dictionary.
    Complexity: O(n)
    """
    pairs = []

    # Dictionary of numbers already seen
    numbers_seen = {}
    second_number = None
    for n in array:
        summing_number = number - n
        if summing_number in numbers_seen:
            pairs.append((n, summing_number))
        else:
            numbers_seen[n] = 1

    return pairs if pairs else None

print(contains_sum_of(10, [3, 4, 1, 2, 2, 5 ,5, 8]))

print(contains_sum_of(10, [3, 4]))
