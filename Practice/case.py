"""case"""

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

    :param word:
    :return:
    """
    if '_' in word:
        return 'snake'
    else:
        return 'camel'


def format_word(case, word):
    """

    >>> format_word('snake', 'my_word')
    'myWord'

    >>> format_word('camel', 'myWord')
    'my_word'

    :param case:
    :param word:
    :return:
    """
    count = 0
    if case == 'snake':

        for index in range(len(word)):
            if word[index] == '_':
                count += 1
        size = len(word) - count;
        for index in range(size):
            if word[index] == '_':
                word = word[:index] + word[index+1:].capitalize()


        return word
    else:
        for index in range(len(word)):
            if word[index].isupper():
                count += 1
            size = len(word) + count
            for index in range(size):
                if word[index].isupper():
                    word = word[:index] + '_' + word[index].lower() + word[index+1:]
        return word


def output_formatted_word(formatted_word):
    print('Your converted word is:' + formatted_word)


def main():
    word = get_input()
    case = test_format(word)
    formatted_word = format_word(case, word)
    output_formatted_word(formatted_word)


main()
