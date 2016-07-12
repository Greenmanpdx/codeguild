"""Pig latin"""
FIRST_LETTER_VOWELS = 'AEIOUaeiou'
OTHER_LETTER_VOWELS = 'aeiouy'
PUNCTUATION = ' ,_-.?!:;'
def convert_to_list(sentence):
    """Takes a sentence and converts into a list"""
    word_list = sentence.split()
    return word_list


def move_letters(word, index):
    letters_to_move = word[:index]

    if word[-1] in PUNCTUATION:
        punctuation = word[-1]
        end_of_word = word[index:-1]
        word = end_of_word + letters_to_move.lower() + 'ay' + punctuation
    else:
        end_of_word = word[index:-1]
        word = end_of_word + letters_to_move.lower() + 'ay'
    return word


def find_index_of_first_vowel(word):
    """Returns the index of the first vowel in the word"""
    if word[0] in FIRST_LETTER_VOWELS:
        return 0
    elif word[1] in FIRST_LETTER_VOWELS:
        return 1
    elif word[2] in FIRST_LETTER_VOWELS:
        return 2
    else:
        return 3


def convert_to_pig_latin(word_list):
    """takes a list of words, converts the words to pig latin, then rejoins them into a sentence"""
    for index in range(len(word_list)):
        first_vowel_index = find_index_of_first_vowel(word_list[index])
        word_list[index] = move_letters(word_list[index], first_vowel_index)

    return word_list


def convert_list_to_string(pig_latin_list):
    sentence = ' '.join(pig_latin_list)
    return sentence

def input_sentence():
    """Prompt the user for a sentence"""
    print('Please enter a sentence: ')
    sentence = input()
    return sentence


def output_sentence(sentence, pig_latin_sentence):
    """Give the user the finished Pig Latin sentence"""
    print(sentence + ' in Pig Latin is ' + pig_latin_sentence)


def main():
    """The controller function"""
    print('Welcome to the English to pig latin translator')
    sentence = input_sentence()
    word_list = convert_to_list(sentence)
    pig_latin_list = convert_to_pig_latin(word_list)
    pig_latin_sentence = convert_list_to_string(pig_latin_list)
    pig_latin_sentence = pig_latin_sentence.capitalize()
    output_sentence(sentence, pig_latin_sentence)


main()




