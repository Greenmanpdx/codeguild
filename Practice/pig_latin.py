"""Pig latin"""
FIRST_LETTER_VOWELS = 'AEIOUaeiou'
OTHER_LETTER_VOWELS = 'aeiouy'
PUNCTUATION = ' ,_-.?!:;'
print('Welcome to the English to pig latin translator')
print('Please enter a sentence: ')
sentence = input()

word_list = sentence.split()

letter_list = list(str(word_list[0]))

# handle the first word since it is capitalized
if letter_list[0] in FIRST_LETTER_VOWELS:
    if letter_list[-1] in PUNCTUATION:
        pig_latin_word = ''.join(letter_list[:-1]) + 'ay' + letter_list[-1]
    else:
        pig_latin_word = ''.join(letter_list) + 'ay'
    word_list[0] = pig_latin_word

elif letter_list[1] in OTHER_LETTER_VOWELS:
    letter_list[1] = str(letter_list[1]).upper()
    letter_list[0] = str(letter_list[0]).lower()
    if letter_list[-1] in PUNCTUATION:
        pig_latin_word = ''.join(letter_list[1:-1]) + letter_list[0] + 'ay' + letter_list[-1]
    else:
        pig_latin_word = ''.join(letter_list[1:]) + letter_list[0] + 'ay'
    word_list[0] = pig_latin_word
elif letter_list[2] in OTHER_LETTER_VOWELS:
    letter_list[0] = str(letter_list[0]).lower()
    letter_list[2] = str(letter_list[2]).upper()
    if letter_list[-1] in PUNCTUATION:
            pig_latin_word = ''.join(letter_list[2:-1]) + ''.join(letter_list[0:2]) + 'ay' + letter_list[-1]
    else:
        pig_latin_word = ''.join(letter_list[2:]) + ''.join(letter_list[0:2]) + 'ay'
    word_list[0] = pig_latin_word
else:
    letter_list[0] = str(letter_list[0]).lower()
    letter_list[3] = str(letter_list[3]).upper()
    if letter_list[-1] in PUNCTUATION:
        pig_latin_word = ''.join(letter_list[3:-1]) + ''.join(letter_list[0:3]) + 'ay' + letter_list[-1]
    else:
        pig_latin_word = ''.join(letter_list[3:]) + ''.join(letter_list[0:3]) + 'ay'
    word_list[0] = pig_latin_word

i = 1  # loop through the words until end of the sentence
while i < len(word_list):
    letter_list = list(str(word_list[i]))
    if letter_list[0] in FIRST_LETTER_VOWELS:
        if letter_list[-1] in PUNCTUATION:
            pig_latin_word = ''.join(letter_list[:-1]) + 'ay' + letter_list[-1]
        else:
            pig_latin_word = ''.join(letter_list) + 'ay'
        word_list[i] = pig_latin_word

    elif letter_list[1] in OTHER_LETTER_VOWELS:
        if str(letter_list[0]).isupper():
            letter_list[0] = str(letter_list[0]).lower()
            letter_list[1] = str(letter_list[1]).upper()
        if letter_list[-1] in PUNCTUATION:
            pig_latin_word = ''.join(letter_list[1:-1]) + letter_list[0] + 'ay' + letter_list[-1]
        else:
            pig_latin_word = ''.join(letter_list[1:]) + letter_list[0] + 'ay'
        word_list[i] = pig_latin_word
    elif letter_list[2] in OTHER_LETTER_VOWELS:
        if str(letter_list[0]).isupper():
            letter_list[0] = str(letter_list[0]).lower()
            letter_list[2] = str(letter_list[2]).upper()
        if letter_list[-1] in PUNCTUATION:
            pig_latin_word = ''.join(letter_list[2:-1]) + ''.join(letter_list[0:2]) + 'ay' + letter_list[-1]
    else:
        if str(letter_list[0]).isupper():
            letter_list[0] = str(letter_list[0]).lower()
            letter_list[3] = str(letter_list[3]).upper()
        if letter_list[-1] in PUNCTUATION:
            pig_latin_word = ''.join(letter_list[3:-1]) + ''.join(letter_list[0:3]) + 'ay' + letter_list[-1]
        else:
            pig_latin_word = ''.join(letter_list[3:]) + ''.join(letter_list[0:3]) + 'ay'
        word_list[i] = pig_latin_word
    i += 1
pig_latin_sentence = ' '.join(word_list)
print(sentence + ' in Pig Latin is ' + pig_latin_sentence)
