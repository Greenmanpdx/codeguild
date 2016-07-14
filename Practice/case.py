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



def snake_to_camel(word):
    """
    snake_to_camel('my_word')
    'myWord'


    :param word:
    :return:
    """

    count = 0
    for index in range(len(word)):
        if word[index] == '_':
            count += 1
    size = len(word) - count
    for index in range(size):
        if word[index] == '_':
                word = word[:index] + word[index+1:].capitalize()
    return word


def camel_to_snake(word):
        """
        camel_to_snake('myWord')
        'my_word'

        :param word:
        :return:
        """

        count = 0
        for index in range(len(word)):
            if word[index].isupper():
                count += 1
            size = len(word) + (count-1)
            for index in range(size):
                if word[index].isupper():
                    word = word[:index] + '_' + word[index].lower() + word[index+1:]
        return word

def kebob_to_snake(word):
    """
    kebob_to_snake('my-word')
    'my_word'

    :param word:
    :return:
    """
    return word.replace('-', '_')


def snake_to_kebob(word):
    return word.replace('_', '-')

def constant_to_snake(word):
    """
    constant_to_snake('MY_WORD')
    'my_world'
    :param word:
    :return:
    """
    return word.lower()

def snake_to_constant(word):
    """

    snake_to_constant('my_word')
    'MY_WORLD'

    :param word:
    :return:
    """
    return word.upper()



def output_formatted_words(snake, camel, kebob, constant):
    print('snake: ' + snake)
    print('camel: ' + camel)
    print('kebob: ' + kebob)
    print('constant: ' + constant)


def main():
    word = get_input()
    case = test_format(word)
    if case == 'snake':
        snake = word;
        camel = snake_to_camel(word)
        kebob = snake_to_kebob(word)
        constant = snake_to_constant(word)
    elif case == 'camel':
        camel = word
        snake = camel_to_snake(word)
        kebob = snake_to_kebob(snake)
        constant = snake_to_constant(snake)
    elif case == 'kebob':
        kebob = word
        snake = kebob_to_snake(kebob)
        camel = snake_to_camel(snake)
        constant = snake_to_constant(snake)
    else:
        constant = word
        snake = constant_to_snake(constant)
        camel = snake_to_camel(snake)
        kebob = snake_to_kebob(snake)

    output_formatted_words(snake, camel, kebob, constant)


main()
