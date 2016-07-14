""" making a sum pairs function"""

def sum_pairs(list_of_numbers, number_to_sum_to):
    """

    >>> sum_pairs([1,2,3,4], 5)
    ['(1,4)', '(2,3)']


    :param list_of_numbers:
    :param number_to_sum_to:
    :return:
    """
    sum_list = []
    for i, number in enumerate(list_of_numbers):
        for k, number2 in enumerate(list_of_numbers[i+1:]):
            if (number + number2) == number_to_sum_to:
                sum_list.append('(' + str(number) + ',' + str(number2) + ')')


    return sum_list
