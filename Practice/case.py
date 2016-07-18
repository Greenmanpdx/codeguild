"""case"""
import re


def get_input():
    """
    Takes the input from the user
    """
    print('Please enter a word to be formatted:')
    return input()


def test_for_format_type(word):
    """

    >>> test_format('my_word')
    'snake'

    >>> test_format('myWord')
    'camel'

    >>> test_format('my-word')
    'kebob'

    >>> test_format('MY_WORD')
    'constant'

    :param word:
    :return: the case as a string
    """
    if '_' in word:
        if word.isupper():
            return 'constant'
        else:
            return 'snake'
    elif '-' in word:
        return 'kebob'
    else:
        return 'camel'




def make_list(case, word):
    """

>>> make_list('snake', 'this_is_a_test')
['this', 'is', 'a', 'test']

>>> make_list('camel', 'ThisIsATest')
['this', 'is', 'a', 'test']

>>> make_list('kebob', 'this-is-a-test')
['this', 'is', 'a', 'test']

>>> make_list('constant', 'THIS_IS_A_TEST')
['this', 'is', 'a', 'test']

    :param case:
    :param word:
    :return:
    """
    if case == 'snake':
        word_list = word.split('_')
    elif case == 'camel':
        word_list = []
        capitalized_word_list = re.findall('[A-Z][^A-Z]*', word)
        for W in capitalized_word_list:
            word_list.append(W.lower())
    elif case == 'kebob':
        word_list = word.split('-')
    else:
        word = word.lower()
        word_list = word.split('_')
    return word_list




def output_formatted_word(snake, camel, kebob, constant):

    print('Snake: ' + snake)
    print('Camel: ' + camel)
    print('Kebob: ' + kebob)
    print('Constant' + constant)

def set_snake(word_list):
    """
    >>> set_snake(['this', 'is', 'a', 'test'])
    'this_is_a_test'

    :param word_list:
    :return: snake as a string
    """
    snake = ('snake: ' + '_'.join(word_list))
    return snake


def set_kebob(word_list):
    """
    >>> set_kebob(['this', 'is', 'a', 'test'])
    'this-is-a-test'

    :param word_list:
    :return: kebob as a string
    """
    kebob = 'kebob: ' + '-'.join(word_list)
    return kebob


def set_camel(word_list):
    """
       >>> camel(['this', 'is', 'a', 'test'])
       'ThisIsATest'

       :param word_list:
       :return: camel as a string
       """
    word_list = [element.title() for element in word_list]
    camel = 'camel: ' + ''.join(word_list)
    return camel


def set_constant(word_list):
    """
    >>> set_constant(['this', 'is', 'a', 'test'])
    'THIS_IS_A_TEST'

    :param word_list:
    :return: constant as a string
    """
    constant = 'constant: ' + ('_'.join(word_list)).upper()
    return constant


def main():
    word = get_input()
    case = test_for_format_type(word)
    word_list = make_list(case, word)

    snake = set_snake(word_list)
    kebob = set_kebob(word_list)
    camel = set_camel(word_list)
    constant = set_constant(word_list)

    output_formatted_word(snake, camel, kebob, constant)


if __name__ == '__main__':
    main()
