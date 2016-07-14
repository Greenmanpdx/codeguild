"""case"""
import re


def get_input():
    """
    Takes the input from the user"""
    print('Please enter a word to be formatted:')
    return input()


def test_format(word):
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
    :return:
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
    if case == 'snake':
        word_list = word.split('_')
    elif case == 'camel':
        word_list = re.findall('[A-Z][^A-Z]*', word)
    elif case == 'kebob':
        word_list = word.split('-')
    else:
        word = word.lower()
        word_list = word.split('_')
    return word_list




def output_formatted_words(word_list):
    """

    >>> output_formatted_words(['this', 'is', 'a', 'test'])
    snake: this_is_a_test
    kebob: this-is-a-test
    camel: ThisIsATest
    constant: THIS_IS_A_TEST

    :param word_list:
    :return:
    """
    print('snake: ' + '_'.join(word_list))
    print('kebob: ' + '-'.join(word_list))
    word_list = [element.title() for element in word_list]
    print('camel: ' + ''.join(word_list))
    print('constant: ' + ('_'.join(word_list)).upper())


def main():
    word = get_input()
    case = test_format(word)
    word_list = make_list(case, word)


    output_formatted_words(word_list)


main()
