"""Mad Libs"""

baseText = open('madlib.txt', 'r')

original = baseText.read()
fin_story = ''


def ad_lib(word):
    phrase = input('Please enter a ', +word)
    return phrase

index = 0
while index < len(original):
    letter = original[index]
    if letter == '{':
        word = ''
        ++index
        wletter = ''
        while wletter != '}':
            wletter = original[index]
            word = word + wletter
            ++original[index]
            phrase = ad_lib(word)
        k = 0
        while k < len(phrase):
            fin_story = fin_story + phrase[k]
    ++index

    fin_story += original[index]

print('Your story: /n' + fin_story)
