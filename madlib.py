"""Mad Libs"""
#import pdb

baseText = open('madlib.txt', 'r')

original = baseText.read(500)

word_list = original.split()


def ad_lib(word):
    print('Please enter a ')
    print(word)
    phrase = input()
    return phrase
i = 0

def main():
    print('Welcome to Sad Libs!')
    while i < len(word_list):
        if '{' in word_list[i]:
            word = ''.join(word_list[i])
            word_list[i] = ad_lib(word)
        i += 1

    print('Your story: /n', ' '.join(word_list))

main()
