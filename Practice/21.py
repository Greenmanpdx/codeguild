"""Black Jack"""

print('Black Jack Advice\n Enter a card\n')
print('Options are: 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K or A.')

card1 = input()

print('What is your second card?')
card2 = input()
ace1 = False
ace2 = False
if card1 == 'J' or card1 == 'K' or card1 == 'Q':
    score1 = 10
elif card1 == 'A':
    ace1 = True
else:
    score1 = int(card1)

if card2 == 'J' or card2 == 'K' or card2 == 'Q':
    score2 = 10
elif card2 == 'A':
    ace2 = True
else:
    score2 = int(card2)

if ace1 is True and ace2 is False:
    if 5 < score2 < 11:
        score1 = 11
    else:
        score1 = 1
if ace2 is True and ace1 is False:
    if 5 < score1 < 11:
        score2 = 11
    else:
        score2 = 2
if ace2 is True and ace1 is True:
    score1 = 11
    score2 = 1
total = score1 + score2
print('\nTotal: ', total)
if total < 17:
    print('Hit')
if 17 <= total < 21:
    print('stay')
if total == 21:
    print('Blackjack!')

print('\nCard 1: ', card1)
print('Card 2: ', card2)
print('score1: ', score1)
print('score2: ', score2)
print('ace1: ', ace1)
print('ace2: ', ace2)
