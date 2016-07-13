"""spelling"""

def get_word_from_user():
    word = input()
    return word


def check_rule(word):
    word_list = list(word)
    i = 0
    while i - 1 < len(word):
        if word_list[i] == 'i':
            if word_list[i + 1] == 'e':
                print(word + ' follows the rule')
                break
        elif word_list[i] == 'e':
            if word_list[i + 1] == 'i':
                print(word + ' does not follow the rule')
                break
        elif i + 1 == len(word):
            print('Invalid word, must contain ie or ei')
            break

        i += 1


def main():
    print('Does your word follow i before e?')
    print('Enter a word')
    word = get_word_from_user()
    check_rule(word)


main()